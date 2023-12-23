
describe('Login Tests', () => {
    it('should show an error message on login with incorrect password', () => {
      cy.visit("http://localhost/orangehrm/web/index.php/login");
      cy.get("input[placeholder='Username']").type('adminn');
      cy.get("input[placeholder='Password']").type('"admin1234"');
      cy.get("button[type='submit']").click();
      cy.get('.error-message').should('contain', 'Invalid credentials');
    });
  
  
    it('should show an error message on login with empty username and password', () => {
      cy.visit('http://localhost/orangehrm/web/index.php/login');
      cy.get("input[placeholder='Username']").clear();
      cy.get("input[placeholder='Password']").clear();
      cy.get("button[type='submit']").click();
      cy.get('.error-message').should('contain', 'Username and Password are required');
    });
  });