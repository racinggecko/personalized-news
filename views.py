from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import NewsSource, UserProfile

@login_required
def news_feed(request):
    user_profile = UserProfile.objects.get(user=request.user)
    subscribed_sources = user_profile.subscribed_sources.all()
    context = {'subscribed_sources': subscribed_sources}
    return render(request, 'news_feed.html', context)

# urls.py (Django)
from django.urls import path
from .views import news_feed

urlpatterns = [
    path('news_feed/', news_feed, name='news_feed'),
]

# news_feed.html (Django template)
{% extends 'base.html' %}

{% block content %}
  <h1>Personalized News Feed</h1>
  <ul>
    {% for source in subscribed_sources %}
      <li>{{ source.name }}</li>
    {% endfor %}
  </ul>
{% endblock %}

# App.js (ReactJS)
import React, { useState, useEffect } from 'react';

function App() {
  const [userProfile, setUserProfile] = useState({});
  const [newsSources, setNewsSources] = useState([]);

  useEffect(() => {
    // Fetch user profile data from API
    fetch('/api/user_profile/')
      .then(response => response.json())
      .then(data => setUserProfile(data));

    // Fetch news sources data from API
    fetch('/api/news_sources/')
      .then(response => response.json())
      .then(data => setNewsSources(data));
  }, []);

  return (
    <div className="App">
      <h1>Personalized News Feed</h1>
      <h2>Subscribed News Sources:</h2>
      <ul>
        {newsSources.map(source => (
          <li key={source.id}>{source.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
