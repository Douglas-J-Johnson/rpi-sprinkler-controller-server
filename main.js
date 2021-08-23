const HIGH = "HIGH";
const LOW = "LOW"

let relayStatuses = {
    Relay1: 1,
    Relay2: 1,
    Relay3: 1,
    Relay4: 1,
    Relay5: 1,
    Relay6: 1,
    Relay7: 1,
    Relay8: 1
};

function setButtonClasses() {
    let relayButton = null;

    Object.keys(relayStatuses).forEach(relayIdentifier => {
        relayButton = document.getElementById(relayIdentifier);

        if (relayStatuses[relayIdentifier] === 1) {
            relayButton.classList.remove(HIGH);
            relayButton.classList.add(LOW);
        }
        else if (relayStatuses[relayIdentifier] === 0) {
            relayButton.classList.remove(LOW);
            relayButton.classList.add(HIGH);
        }
    });
}

function buttonClick(relayIdentifier) {
    if(relayStatuses[relayIdentifier] === 1) { relayStatuses[relayIdentifier] = 0; }
    else if(relayStatuses[relayIdentifier] === 0) { relayStatuses[relayIdentifier] = 1; }
    
    setButtonClasses()
    // $.post('Relay', relayStatuses);
}

setButtonClasses();
