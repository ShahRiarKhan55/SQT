describe('OrangeHRM URL and Title Testing', () => {
    
    it('should have a valid URL and title after successful login', () => {
      
        cy.visit("http://localhost/orangehrm/web/index.php/login");
      cy.get("input[placeholder='Username']").type('Admin');
      cy.get("input[placeholder='Password']").type('admin123');
      cy.get("button[type='submit']").click();
      cy.url().should('include', 'http://localhost/orangehrm/web/index.php/dashboard/index');
      cy.title().should('eq', 'OrangeHRM');
  
    });
  
    it('should handle invalid login and check URL and title', () => {
        cy.visit("http:/localhost/oranghrm/web/index.php/login");
    
        cy.get("input[placeholder='Username']").type('saf');
        cy.get("input[placeholder='Password']").type('saf12');
        cy.get("button[type='submit']").click();
        cy.url().should('not.include', 'http://localhost/orangehrm/web/index.php/dashboard/index');
        cy.title().should('eq', 'OrangeHRM - New Level of HR Management');
    
      });
  });