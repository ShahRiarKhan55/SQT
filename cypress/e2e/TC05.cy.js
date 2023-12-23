describe('OrangeHRM Add Employee Test', () => {
    it('should add a new employee', () => {
      
      cy.visit("http://localhost/orangehrm/web/index.php/login");
      cy.get("input[placeholder='Username']").type('Admin');
      cy.get("input[placeholder='Password']").type('admin123');
      cy.get("button[type='submit']").click();
  
    
      cy.contains('PIM').click();
      cy.contains('Add Employee').click();
  
      
      cy.get("input[name='firstName']").type('John');
      cy.get("input[name='lastName']").type('Doe');
      cy.get("input[name='employeeId']").type('EMP123');
  
      
      cy.contains('Save').click();
  
      
      cy.get('.message.success').should('contain', 'Successfully Saved');
  
    
    });
    it('should remove an employee', () => {
     
      cy.visit("http://localhost/orangehrm/web/index.php/login");
  
      
      cy.get("input[placeholder='Username']").type('Admin');
      cy.get("input[placeholder='Password']").type('admin123');
      cy.get("button[type='submit']").click();
  
      
      cy.contains('PIM').click();
      cy.contains('Employee List').click();
  
      
      cy.get("input[name='empsearch[employee_name][empName]']").type('John Doe');
      cy.contains('Search').click();
      cy.contains('John Doe').parent('td').siblings('td').find("input[type='checkbox']").check();
  
      
      cy.contains('Delete').click();
  
      
      cy.get('#dialogDeleteBtn').click();
  
      
      cy.get('.message.success').should('contain', 'Successfully Deleted');
  
      
    });
  });