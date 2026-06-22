# Curriculum Design Engine
A curriculum design engine that allows administrators to create and sequence modules, define prerequisites, and publish/unpublish curricula.

## Usage
1. Create a new curriculum: `engine.create_curriculum("Test Curriculum", "This is a test curriculum")`
2. Add a module: `engine.add_module("Test Curriculum", "Test Module", "This is a test module")`
3. Edit a module: `engine.edit_module("Test Curriculum", "Test Module", "New Test Module", "This is a new test module")`
4. Delete a module: `engine.delete_module("Test Curriculum", "Test Module")`
5. Reorder modules: `engine.reorder_modules("Test Curriculum", ["Test Module 2", "Test Module 1"])`
6. Define prerequisites: `engine.define_prerequisites("Test Curriculum", "Test Module", ["Prerequisite 1", "Prerequisite 2"])`
7. Publish a curriculum: `engine.publish_curriculum("Test Curriculum")`
8. Unpublish a curriculum: `engine.unpublish_curriculum("Test Curriculum")`
9. Get the curriculum data as JSON: `engine.to_json()`
