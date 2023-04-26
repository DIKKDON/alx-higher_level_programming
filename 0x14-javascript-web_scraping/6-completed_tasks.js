#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) process.exit(1);

  const tasks = JSON.parse(body);
  const completedTasks = {};
  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) completedTasks[task.userId]++;
      else completedTasks[task.userId] = 1;
    }
  }
  console.log(completedTasks);
});
