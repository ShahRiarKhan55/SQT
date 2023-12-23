///<reference types="cypress" />

describe("OrangeHRM Login Test", () => {

    it("verify title positive", () => {
        cy.visit(
            "http://localhost/orangehrm/web/index.php/login"
        );
        cy.title().should("eq", "OrangeHRM");
    });



});
   it("verify title positive", () => {
    cy.visit(
        "http://localhost/orangehrm/web/index.php/login"
    );
    cy.title().should("eq", "OrangeHRM");
});


