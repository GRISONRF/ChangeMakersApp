const all_causes = [
    {
        cause_id: 1,
        cause_name: "humans" ,
        cause_title: "Advocacy and Human Rights",
        cause_icon: "/static/images/humansrights.png",
    },
    {
        cause_id: 2,
        cause_name: "animals",
        cause_title: "Animals",
        cause_icon: "/static/images/animals.png",
    },
    {
        cause_id: 3,
        cause_name: "arts",
        cause_title: "Arts and Culture",
        cause_icon: "/static/images/arts.png",
    },
    {
        cause_id: 4,
        cause_name: "child",
        cause_title: "Children and Youth",
        cause_icon: "/static/images/children.png",
    },
    {
        cause_id: 5,
        cause_name: "education",
        cause_title: "Education",
        cause_icon: "/static/images/education.png",
    },
    {
        cause_id: 6,
        cause_name: "enviromnent",
        cause_title: "Environment",
        cause_icon: "/static/images/environment.png",
    },
    {
        cause_id: 7,
        cause_name: "hunger",
        cause_title: "Hunger",
        cause_icon: "/static/images/hunger.png",
    },
    {
        cause_id: 8,
        cause_name: "homeless",
        cause_title: "Homeless and Housing",
        cause_icon: "/static/images/homeless.png",
    },
    {
        cause_id: 9,
        cause_name: "immigrants",
        cause_title: "Immigrants and Refugees",
        cause_icon: "/static/images/immigrants.png",
    },
    {
        cause_id: 10,
        cause_name: "lgbqt",
        cause_title: "LGBTQ+",
        cause_icon: "/static/images/lgbqt.png",
    },
    {
        cause_id: 11,
        cause_name: "race",
        cause_title: "Race and Ethnicity",
        cause_icon: "/static/images/race.png",
    },
    {
        cause_id: 12,
        cause_name: "women",
        cause_title: "Women",
        cause_icon: "/static/images/women.png",
    },
    {
        cause_id: 13,
        cause_name: "other",
        cause_title: "Other",
        cause_icon: "/static/images/other.png",
    },
];

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
                <p>By: {props.inst_name}</p>
                <p>{props.evt_date}</p>
                <p>{props.evt_city}, {props.evt_state}</p>
                <p>{props.cause.cause_title}</p>
                <a href={`/events/${props.event_id}`}> 
                    <button>More details</button>
                </a>   
            </div>
        </div>
    );
}


function EventCardContainer() {
    const [city, setCity] = React.useState('');
    const [state, setState] = React.useState('');
    const [cause, setCause] = React.useState('');
    const [searchResults, setSearchResults] = React.useState('');

    
    function addEventCard(){
        fetch("/search_results.json", { 
            method: "POST",
            headers: {
                "Content-Type": "application/json", 
            },
            body: JSON.stringify({ city, state, cause}),
        })
        .then( (response) => { 
           
            return response.json(); })
        .then((jsonResponse) => {
                                       
            setSearchResults(jsonResponse);
        });
    }
        
        const causeButtons = [];
        for (const causeButton of all_causes) {     
            causeButtons.push(
                <button className="react-btn" key={ causeButton.cause_id } name={ causeButton.cause_name } type="submit" onClick = {() => {setCause(causeButton.cause_name)}}> 
                    <img key={ causeButton.cause_name } src={ causeButton.cause_icon } height ="30" width="50" />
                </button>
            );
        }  

        const eventCards = [];
        for (const sResult of searchResults) {
            eventCards.push(
                <EventCard
                    key={sResult.event_id}
                    evt_title={sResult.evt_title}
                    inst_name={sResult.inst_name}
                    evt_city={sResult.evt_city}
                    evt_state={sResult.evt_state}    
                    cause={sResult.cause}
                    evt_date={sResult.evt_date}
                    event_id={sResult.event_id}
                    evt_pic={sResult.evt_pic}
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
                <div className="state-input">
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
            </div>

            <div className="cause-container">
                <div className="p-cause">
                    <p>Cause:</p>
                </div>
               <div className="cause-btns">
                    {causeButtons} 
                </div>
            </div>
            
            
            <button type="submit" className="btn-find" onClick={addEventCard}>Find</button>

            <div className="cards-container">
                {eventCards}
            </div>
                           
        </React.Fragment>
    )
}

ReactDOM.render(<EventCardContainer />, document.getElementById('events-container'));

// ------------------------------- recommended events by city, state and skills ---------------------------- \\


function RecommendedEventsCards(props) {
    return (
        <div className="card"> 
            <div className="image">
                <img src={props.evt_pic}></img>
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



function RecommendedEventsContainer() {
    const [recommendedResults, setRecommendedResults] = React.useState('');
    

    console.log(recommendedResults)
    const recommendationCards = []
    for (const recResult of recommendedResults) {
            recommendationCards.push(
                <RecommendedEventsCards
                    key={recResult.event_id}
                    evt_title={recResult.evt_title}
                    inst_name={recResult.inst_name}    
                    evt_city={recResult.evt_city}
                    evt_state={recResult.evt_state}    
                    cause={recResult.cause}
                    evt_date={recResult.evt_date}
                    event_id={recResult.event_id}
                    evt_pic={recResult.evt_pic}
                    // skills={recResult.skills}
                />
            )
        }
 
    
    const handleClick =  () => {
        fetch('/search_recommended.json', {
            method: "POST",
            headers: {
                "Content-Type": "application/json", 
            },
            body: JSON.stringify({ recommendedResults }),
        })
      
        .then( (response) => { 
            return response.json(); })

        .then((jsonResponse) => {                                    
            setRecommendedResults(jsonResponse);
        });
    };
    
    
    return (
        <div>
            <button onClick={handleClick}> Recommended Events </button>

         
            <div>
            {recommendationCards}               
            </div>
    
        </div>
    )
    

}

ReactDOM.render(<RecommendedEventsContainer />, document.getElementById('recommended-events'));