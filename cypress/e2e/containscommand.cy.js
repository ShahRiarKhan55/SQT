describe('contains command' , ()=>{
    it('Verify login validation', ()=> {
        cy.visit("http://localhost/orangehrm/web/index.php/login");
        
        cy.get("input[placeholder='Username']").type("Admin");
        
        cy.get("input[placeholder='Password']").type("admin123");
        
        cy.get("button[type='submit']").click();
        cy.get(':nth-child(1) > .oxd-main-menu-item > .oxd-text').click();
        cy.get('.oxd-topbar-body-nav > ul').contains('job', {matchCase : false}).click();

    })

  
  })