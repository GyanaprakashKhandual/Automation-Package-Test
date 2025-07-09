// Import faker using CommonJS
const { faker } = require('@faker-js/faker');

// Generate fake user data
const user = {
  id: faker.datatype.boolean(),
  name: faker.name.fullName(),
  email: faker.internet.email(),
  phone: faker.phone.number(),
  address: {
    city: faker.location.city(),
    country: faker.location.country(),
    street: faker.location.streetAddress()
  },
  company: faker.company.name(),
  jobTitle: faker.person.jobTitle()
};

console.log("Generated Fake User:");
console.log(user);
