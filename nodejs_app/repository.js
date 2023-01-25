const Pool = require("pg").Pool;

const pool = new Pool({
  user: 'postgres',
  host: 'postgres',
  database: 'uns',
  password: 'ftn',
  port: 5432,
});

const createProfessor = (request, response) => {
  const user = request.body;
  createUser(user, "PROFESSOR", response);
};
const createStudent = (request, response) => {
  const user = request.body;
  createUser(user, "STUDENT", response);
};

function createUser(user, user_type, response) {
  pool.query(
    "INSERT INTO users (jmbg, name, user_type) VALUES ($1,$2,$3) RETURNING *",
    [user.jmbg, user.name, user_type],
    (error, result) => {
      if (error) {
        response
          .status(500)
          .send(`JMBG: ${user.jmbg} already exists!`);
      } else {
        response
          .status(201)
          .send(`JMBG: ${user.jmbg} successfully created!`);
      }
    }
  );
}

module.exports = {
  createProfessor,
  createStudent,
};