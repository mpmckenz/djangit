    <h1>DEV NOTES for homepage:</h1>
    <h2>navbar</h2>
    <p>
      SORT OPTIONS: 1. vote count 2. ALL posts 3. communities you joined 4.
      users you follow
    </p>
    <p>
      SEARCH BAR: return results of usernames or community_names that contain
      search input
    </p>
    <p>
      user to user direct messaging
    </p>
    <p>
      MY PROFILE: 1. posts (shows your posts you wrote) 2. comments (shows your
      comments on other people posts) 3. upvoted (shows posts of ones you
      upvoted) 4. downvoted (shows posts of ones you downvoted)
    </p>
    <p>
      create community and become moderator of that community (ability to delete
      other users posts in your community)
    </p>
    <h2>homepage body</h2>
    <p>posts of followed users and joined communities</p>
    {% for item in joinedcommunity %} {% for post in followeduser %} {%endfor%}
    {%endfor%}
    <h2>post details (see card div below)</h2>
    <p>
      note: each post is wrapped in an a tag to make entire div clickable going
      to post
    </p>
    <a href="">
      <div class="card">
        <a href="">Community link to all commumity posts</a><br />
        <a href="">User link to all their posts</a>
        <p>timestamp here</p>
        <p>Djangit Title Here</p>
        <p>Djangit message body here</p>
        <p>number of comments of this post</p>
        <p>upvote option</p>
        <p>(sum of upvotes - downvotes)</p>
        <p>downvote option</p>
      </div>
    </a>
