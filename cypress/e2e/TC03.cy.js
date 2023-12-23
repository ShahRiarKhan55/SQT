

describe('OrangeHRM Login Tests', () => {
    it('should allow login with a valid username and password', () => {
      cy.visit("http://localhost/orangehrm/web/index.php/login");
  
     
      cy.get("input[placeholder='Username']").type("Admin");
  
      cy.get("input[placeholder='Password']").type("admin123");
      cy.get("button[type='submit']").click();
      cy.url().should('include', 'http://localhost/orangehrm/web/index.php/dashboard/index');
    });
  
    it('should show an error message for invalid username', () => {
      cy.visit("http://localhost/orangehrm/web/index.php/login");
      cy.get("input[placeholder='Username']").type('admn');
      cy.get("input[placeholder='Password']").type('admin123');
      cy.get("button[type='submit']").click();
      cy.get('#spanMessage').should('contain', 'Invalid credentials');
    });
  });