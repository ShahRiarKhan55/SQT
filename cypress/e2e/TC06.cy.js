describe('Leave Management Tests', () => {
    it('should apply for leave and check leave balance', () => {
      
      cy.visit("http://localhost/orangehrm/web/index.php/login");
  
      cy.get("input[placeholder='Username']").type('Admin');
      cy.get("input[placeholder='Password']").type('admin123');
      cy.get("button[type='submit']").click();
      cy.contains('Leave').click();
      cy.contains('Apply').click();
      
      cy.get("input[name='applyleave[txtLeaveType]']").select('Vacation');
      cy.get("input[name='applyleave[txtFromDate]']").type('2023-12-01');
      cy.get("input[name='applyleave[txtToDate]']").type('2023-12-05');
      cy.get("textarea[name='applyleave[txtComment]']").type('Vacation Leave Request');
      cy.contains('Apply').click();
      cy.get('.message.success').should('contain', 'Leave applied successfully');
  

      cy.contains('My Leave').click();
  
      
      cy.get('.leavebalance').should('contain', 'Balance: 5 days'); 
  
      
    });
});