function EventCard(props) {
    return (
        <div className="card"> 
            <div className="image">
                <img src={`${props.evt_pic}`}></img>
            </div>         
            <div className="title">
                <h1>{props.evt_title}</h1>
            </div>
            <div className="des">
                <p>{props.inst_name}</p>
                <p>{props.evt_city}, {props.evt_state}</p>
                <p>{props.cause}</p>
                <a href={`/events/${props.event_id}`}> 
                    <button>More details</button>
                </a>   
            </div>
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
                    evt_pic={barResult.evt_pic}
                />
            )
        }

    return (
        <React.Fragment>

            <div className="search-inputs">
                <div className="city-input">
                    <label htmlFor="cityInput">
                        City:
                        <input
                        value={city}
                        onChange={(event) => setCity(event.target.value)}
                        id="cityInput"
                        style={{ marginLeft: '5px' }}
                        />
                    </label>
                </div>
            <div className="state-input"></div>
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
            
            <button type="submit" className="react-submit btn-find" onClick={addEventBarCard}>Search Events</button>
            
            
            <div className="all-events-cards">
                {eventCards}        
            </div>

        </React.Fragment>
    )
}
console.log('**************')
ReactDOM.render(<EventBarContainer />, document.getElementById('all-events'));