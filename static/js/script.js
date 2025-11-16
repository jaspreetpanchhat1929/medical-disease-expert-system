let selectedSymptoms = new Set();

function updateSymptomCount() {
    document.getElementById('symptomCount').textContent = selectedSymptoms.size;
}

document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.symptom-checkbox');
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const card = this.closest('.symptom-card');
            
            if (this.checked) {
                selectedSymptoms.add(this.value);
                card.classList.add('selected');
            } else {
                selectedSymptoms.delete(this.value);
                card.classList.remove('selected');
            }
            
            updateSymptomCount();
        });
    });
});

async function diagnoseDisease() {
    const patientName = document.getElementById('patientName').value.trim();
    
    if (!patientName) {
        alert('Please enter patient name');
        return;
    }
    
    if (selectedSymptoms.size === 0) {
        alert('Please select at least one symptom');
        return;
    }
    
    try {
        const response = await fetch('/diagnose', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                patient_name: patientName,
                symptoms: Array.from(selectedSymptoms)
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showReport(data);
        } else {
            alert(data.message);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

function showReport(data) {
    document.getElementById('inputSection').classList.add('d-none');
    document.getElementById('reportSection').classList.remove('d-none');
    
    document.getElementById('reportPatientName').textContent = data.patient_name;
    document.getElementById('reportDate').textContent = new Date(data.date).toLocaleString();
    
    const resultsContainer = document.getElementById('diagnosisResults');
    const diagnosis = data.diagnosis;
    
    if (diagnosis.detected.length > 0) {
        let html = '';
        
        diagnosis.detected.forEach(disease => {
            const colorClass = disease.color === 'danger' ? 'danger' : 'warning';
            html += `
                <div class="card border-${colorClass} mb-3">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-9">
                                <h4 class="text-${colorClass}">${disease.name}</h4>
                                <p>${disease.description}</p>
                            </div>
                            <div class="col-md-3 text-end">
                                <div class="confidence-badge text-${colorClass}">${disease.confidence}%</div>
                                <small class="text-muted">Confidence</small>
                            </div>
                        </div>
                        <div class="alert alert-info mt-3 mb-0">
                            <h6><i class="fas fa-check-circle me-2"></i>Recommendations</h6>
                            <p class="mb-0">${disease.recommendation}</p>
                        </div>
                    </div>
                </div>
            `;
        });
        
        html += `
            <div class="alert alert-warning">
                <h6><i class="fas fa-exclamation-triangle me-2"></i>Medical Disclaimer</h6>
                <p class="mb-0">This is a preliminary diagnosis. Please consult a qualified healthcare professional.</p>
            </div>
        `;
        
        resultsContainer.innerHTML = html;
    } else {
        resultsContainer.innerHTML = `
            <div class="alert alert-secondary text-center">
                <h5>No Disease Detected</h5>
                <p class="mb-0">The symptoms don't match Malaria or Typhoid criteria.</p>
            </div>
        `;
    }
    
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function resetForm() {
    selectedSymptoms.clear();
    document.querySelectorAll('.symptom-checkbox').forEach(cb => {
        cb.checked = false;
        cb.closest('.symptom-card').classList.remove('selected');
    });
    document.getElementById('patientName').value = '';
    updateSymptomCount();
    document.getElementById('inputSection').classList.remove('d-none');
    document.getElementById('reportSection').classList.add('d-none');
    window.scrollTo({top: 0, behavior: 'smooth'});
}