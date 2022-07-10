'use-strict';
// ---------------- comment and review modal button ---------------- \\


// at this button I'll add an event listener
// do a fetch request
// send the info to server.py and save the comment and review on my db
// return the information as a dict
// get the response at .then() 
// display the comment on page

/* what I need to create a new comment and review | where to get it

comment text     |      
review rate    |    
inst_id    |     document.querySelector('#inst-id').innerText;
volunteer_id    |    session



*/
const inst_id = document.querySelector('#inst-id').innerText;
const volunteer_id = document.querySelector('#volunteer-id').innerText;

const commentForm = document.querySelector('#comment-form');
commentForm.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const instRate = document.querySelector('#rate-inst').value;
    const instComment = document.querySelector('#comment-inst').value;

    const instReviewInfo = {
        comment: instComment,
        review: instRate,
        inst_id: inst_id,
        volunteer_id: volunteer_id,
    };

    fetch(`/inst_profile/${inst_id}/review`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(instReviewInfo),
    })

        .then((response) => {

            return response.json(); })
        .then((comment) => {
            alert('Your comment was submitted!');
            console.log(comment.comment_id);

            let commentDiv;

            commentDiv = document.querySelector('.comment-div');

            if (!commentDiv) {
                commentDiv = document.createElement('div');
                commentDiv.setAttribute('id', `${comment.comment_id}`);
                commentDiv.setAttribute('class', `${comment-div}`);
            };

            commentDiv.insertAdjacentHTML(
                'afterbegin',
                `<div id="${comment.comment_id}" class="comment-block">
                <p id="comment-volunteer-name">${comment.volunteer_id}</p>
                <p id="inst-review">Rate: ${comment.review}</p>
                <p>${comment.comment}</p> `
            );

            no_comment = document.querySelector('#no-comment');
            if (no_comment) {
                no_comment.style.display = 'none';
            };   

            const newDeleteBtn = document.getElementById(
                `delete-${comment.comment_id}`,
            );

            console.log(newDeleteBtn.value);
            newDeleteBtn.addEventListener('click', saveDelete)

        });
});



function deleteComment() {
    const deleteCommentBtn = document.querySelectorAll('.delete-comment-btn');
    for (const deleteBtn of deleteCommentBtn) {
      deleteBtn.addEventListener('click', (evt) => {
        evt.preventDefault();
        saveDelete(evt);
      });
    }
}


function saveDelete(evt) {
    evt.preventDefault();

    const deleteComment = evt.target.value;
  
    fetch(`/inst_profile/${deleteComment}/delete`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(deleteComment),
    })
      .then((response) => response.text())
      .then((volunteer_id) => {
        console.log(deleteComment)
        comment = document.getElementById(`${deleteComment}`);
        comment.remove();
        deleteBtn = document.getElementById(`delete-${deleteComment}`);
        deleteBtn.remove();


        commentBlock = document.querySelector('#comment-container');
  
        if (commentBlock.innerText === '') {
          commentBlock.insertAdjacentHTML(
            'afterend',
            '<p id="no-comment"><i>Be the first one to comment</i></p>',
          );
        }
      });
};


    
deleteComment();