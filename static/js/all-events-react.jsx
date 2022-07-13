function EventCard(props) {
    return (
        <div className="card">          
            <div className="title">
                <h1>{props.evt_title}</h1>
            </div>
            <p>{props.inst_name}</p>
            <p>{props.evt_city}, {props.evt_state}</p>
            <p>{props.cause}</p>
            <a href={`/events/${props.event_id}`}> 
                <button>More details</button>
            </a>            
        </div>
    );
}


function EventBarContainer() {
    const [city, setCity] = React.useState('');
    const [state, setState] = React.useState('');
    const [searchBarResults, setSearchBarResults] = React.useState('');
    
    
    function addEventBarCard(){
        fetch("/search_bar.json", { 
            method: "POST",
            headers: {
                "Content-Type": "application/json", 
            },
            body: JSON.stringify({ city, state }),   
        })
        .then( (response) => { 
           
            return response.json(); })
        .then((jsonResponse) => {
                                       
            setSearchBarResults(jsonResponse);
        });
    }
        

        const eventCards = [];
        for (const barResult of searchBarResults) {
            eventCards.push(
                <EventCard
                    key={barResult.event_id}
                    evt_title={barResult.evt_title}
                    inst_name={barResult.inst_name}
                    evt_city={barResult.evt_city}
                    evt_state={barResult.evt_state}    
                    cause={barResult.cause}
                    evt_date={barResult.evt_date}
                    event_id={barResult.event_id}
                />
            )
        }

    return (
        <React.Fragment>

        <div>
            <label htmlFor="cityInput">
                City:
                <input
                value={city}
                onChange={(event) => setCity(event.target.value)}
                id="cityInput"
                style={{ marginLeft: '5px' }}
                />
            </label>

            <label htmlFor="stateInput">
                State: 
                <input
                value={state}
                onChange={(event) => setState(event.target.value)}
                id="stateInput"
                style={{ marginLeft: '5px' }}
                />
            </label>
        </div>

            <button type="submit" className="btn-find" onClick={addEventBarCard}>Search Events</button>
            
        <div>
            {eventCards}        
        </div>

        </React.Fragment>
    )
}
console.log('**************')
ReactDOM.render(<EventBarContainer />, document.getElementById('all-events'));