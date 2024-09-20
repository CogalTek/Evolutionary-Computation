import { exec } from 'child_process';

export default defineEventHandler(async (event) => {
  return new Promise((resolve, reject) => {
    exec('python3 ../main.py -n 5', (error, stdout, stderr) => {
      if (error) {
        reject({ error: error.message });
      } else if (stderr) {
        reject({ error: stderr });
      } else {
        resolve({ output: stdout });
      }
    });
  });
});
