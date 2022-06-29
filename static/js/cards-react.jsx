const all_causes = [
    {
        cause_id: 1,
        cause_name: "humans" ,
        cause_title: "Advocacy and Human Rights",
        cause_icon: "static/images/humansrights.png",
    },
    {
        cause_id: 2,
        cause_name: "animals",
        cause_title: "Animals",
        cause_icon: "static/images/animals.png",
    },
    {
        cause_id: 3,
        cause_name: "arts",
        cause_title: "Arts and Culture",
        cause_icon: "static/images/arts.png",
    },
    {
        cause_id: 4,
        cause_name: "child",
        cause_title: "Children and Youth",
        cause_icon: "static/images/children.png",
    },
    {
        cause_id: 5,
        cause_name: "education",
        cause_title: "Education",
        cause_icon: "static/images/education.png",
    },
    {
        cause_id: 6,
        cause_name: "enviromnent",
        cause_title: "Environment",
        cause_icon: "static/images/environment.png",
    },
    {
        cause_id: 7,
        cause_name: "hunger",
        cause_title: "Hunger",
        cause_icon: "static/images/hunger.png",
    },
    {
        cause_id: 8,
        cause_name: "homeless",
        cause_title: "Homeless and Housing",
        cause_icon: "static/images/homeless.png",
    },
    {
        cause_id: 9,
        cause_name: "immigrants",
        cause_title: "Immigrants and Refugees",
        cause_icon: "static/images/immigrants.png",
    },
    {
        cause_id: 10,
        cause_name: "lgbqt",
        cause_title: "LGBTQ+",
        cause_icon: "static/images/lgbqt.png",
    },
    {
        cause_id: 11,
        cause_name: "race",
        cause_title: "Race and Ethnicity",
        cause_icon: "static/images/race.png",
    },
    {
        cause_id: 12,
        cause_name: "women",
        cause_title: "Women",
        cause_icon: "static/images/women.png",
    },
    {
        cause_id: 13,
        cause_name: "other",
        cause_title: "Other",
        cause_icon: "static/images/other.png",
    },
];

function EventCard(props) {
    return (
        <div class="card">          
            <div class="title">
                <h1>{props.evt_title}</h1>
            </div>
            <p>{props.inst_name}</p>
            <p>{props.evt_location}</p>
            <p>{props.cause}</p>
            <a href="/events/{props.event_id}"> 
                <button>More details</button>
            </a>            
        </div>
    );
}

function EventCardContainer() {
    const [city, setCity] = React.useState('');
    const [cause, setCause] = React.useState('');
    const [searchResults, setSearchResults] = React.useState('');

    
    function addEventCard(){
        fetch("/search_results.json", { 
            method: "POST",
            headers: {
                "Content-Type": "application/json", 
            },
            body: JSON.stringify({"city": city, "cause": cause, "searchResults": searchResults}),
        })
        .then((response) => response.json())
        .then((jsonResponse) => {
            setSearchResults(jsonResponse)
                                         
        });
    }
        
        for (const cause in all_causes) { 
            <>
            <input name="cause" value= { cause.cause_id } hidden/>
            <button name= { cause.cause_name } type="submit" onClick={setCause}> 
                <img src= { cause.cause_icon } height ="30" width="50" />
            </button>
            </>
        } 

        const eventCards = []

        for (const sResult of searchResults) {
            eventCards.push(
                <EventCard
                    evt_title={sResult.evt_title}
                    inst_name={sResult.inst_name}    
                    evt_location={sResult.evt_location}
                    cause={sResult.cause}
                    evt_date={sResult.evt_date}
                    event_id={sResult.event_id}
                />
            )
        }

    return (
        <React.Fragment>
          
            <label htmlFor="cityInput">
                City
                <input
                value={city}
                onChange={(event) => setCity(event.target.value)}
                id="cityInput"
                style={{ marginLeft: '5px' }}
                />
            </label>

            <label htmlFor="cityInput">
                City
                <input
                value={city}
                onChange={(event) => setCity(event.target.value)}
                id="cityInput"
                style={{ marginLeft: '5px' }}
                />
            </label>

            <button type="submit" class="btn-find" onClick={addEventCard}>Find</button>
                            
        </React.Fragment>
    )
}

ReactDOM.render(<EventCardContainer />, document.getElementById('events-container'));