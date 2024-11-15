![image](https://github.com/user-attachments/assets/43b2ab64-e5d6-4386-a393-0c23047b14b9)

### SuperUser access
username: Christy
Password - Kildare89


# Gymstitute

Gymstitute is your one-stop online platform for all things fitness. Whether you're a beginner or a fitness enthusiast, Gymstitute provides a streamlined experience to access a wide range of gym essentials in one convenient place. From high-quality clothing and gear to electronics and personalized, subscription-based meal and workout plans, Gymstitute has everything you need to support your fitness journey.

## Key Features

### Comprehensive Product Range: 

Browse and purchase clothing, gym equipment, and fitness electronics, carefully curated to meet your training needs.

### Subscription-Based Plans:
Access tailored meal plans and workout routines designed to fit your goals, whether you're aiming to build muscle, lose weight, or improve endurance.

### User-Friendly Interface: 
Easily navigate through product categories and subscription services, making it simple to find what you need.

### Project Goal
The goal of Gymstitute is to consolidate all fitness essentials into one easy-to-use platform, saving users time and effort by centralizing everything they need for their gym and fitness journey.

# Features

## Registration and Login
Gymstitute provides a seamless registration and login experience, allowing users to create accounts, log in, and manage their profile effortlessly.

Users can easily sign up for an account and log in to access additional features. I have implemented Django Allauth to streamline the registration and authentication process, supporting both traditional username/password. Cirspy forms is used on login and sign up forms to help with inline consistency.


![image](https://github.com/user-attachments/assets/0aa1198e-5f26-46a4-b453-8a4370b87557)

## Account-Free Purchases: 
While users do not need an account to browse or purchase products, an account is required to access subscription-based meal plans and workout plans.

## Secure Authentication: 
Django Allauth offers secure and reliable authentication, ensuring user data is protected during registration and login.

### How to Use
Creating an Account: Click on the Sign Up button on the website and fill in the required information. Django Allauth takes care of user verification if enabled.

A dynamic scoller option has been added to the signup form page to ho help with overlay.
![image](https://github.com/user-attachments/assets/7318cfb3-a801-47d1-9f10-6fce89e78e39)

Logging In: After registration, users can log in with their credentials. Once logged in, they gain access to exclusive features like subscription management.

![image](https://github.com/user-attachments/assets/4afdbaff-2318-49ca-8cec-55620a6a6458)

### Managing Account:
Users can update their profile and manage subscription preferences directly from their subscription/profile dashboard and also view their order history.

![image](https://github.com/user-attachments/assets/05289108-9d40-4150-bee0-5894c181ab91)

A dynamic scoller also added to the order hsitory for when users reah over 3 orders.

![image](https://github.com/user-attachments/assets/f24260af-3d6a-43e9-9454-acf44891fa59)
![image](https://github.com/user-attachments/assets/59ec023c-b268-48c2-b9a8-3b4b2928acb7)

## Bag Functionality

Gymstitute offers a dynamic and user-friendly shopping experience with a shopping bag feature that updates in real-time as users add or remove items. Both users who are logged in and non-logged-in guests can interact with the bag, making it easy to keep track of products while shopping. They will also get message if adding to the bag was successful or not.

### Key Features of the Bag:

#### Adding Items: 
As users browse the website, they can easily add products (such as clothing, equipment, or electronics) to their bag by clicking the Add to Bag button on each product details page. Users also have the function to return shopping to continue adding items if they so choose.

![image](https://github.com/user-attachments/assets/41e67abc-1f59-4014-b945-4f9498a3fc3d)



### Real-Time Updates:

Each time an item is added to the bag, the basket icon on the website's header updates instantly, reflecting the current total cost of the items in the bag.
![image](https://github.com/user-attachments/assets/6721f80c-9e99-4e00-9759-4d1c687ef12a)


### Viewing the Bag: 

Users can click the basket icon at any time to view the items they’ve added to their bag. This action will display a summary of the bag contents, including:
A list of items with their names, quantities, and individual prices.
The total cost of all items currently in the bag.

![image](https://github.com/user-attachments/assets/c97d53d0-bdf9-4df1-9fb7-bb02a0750725)

![image](https://github.com/user-attachments/assets/dc656b37-4e0e-45f8-94a6-a30616585a83)


### Managing the Bag:
Removing Items: Users can remove individual items from their bag directly from the bag summary page. This will automatically update the total price and the basket icon in real time.

![image](https://github.com/user-attachments/assets/e2fba2f2-ee49-424d-9fdf-cc4e66f30f56)


### Final Total: 

The total of all items in the bag is always displayed, making it easy for users to review their shopping choices before moving to checkout.

### Checkout:
Once satisfied with their selections, users can click on the Proceed to Checkout button to start the checkout process and complete their purchase.

![image](https://github.com/user-attachments/assets/e7ad25ac-4f7a-4846-a2dd-f6a8e5adabf7)

## Checkout Process

Gymstitute’s checkout process is designed to be simple, transparent, and efficient. At checkout, users can review their order, enter delivery details, and complete their purchase. Here’s a breakdown of the key features:

### Key Features of the Checkout Process:

Users who are signed in will have their saved delivery address pre-populated in the checkout form, saving time and reducing errors. However, they can still modify the address if necessary.
Non-signed-in users will be prompted to enter their delivery details manually.

![image](https://github.com/user-attachments/assets/0ecf1697-15f3-4c54-8005-c937ec9873cc)


### Order Summary:

At checkout, users will see a comprehensive breakdown of their order, including the list of items, their quantities, individual prices, and total cost.
Total Amount: The total price of the order is clearly displayed, along with an indicator showing how much the card will be charged.

![image](https://github.com/user-attachments/assets/2052f22d-d301-4d84-a422-b6765eba1968)

Adjust Bag Option:

Users can review their order and have the option to go back and adjust the bag if they wish to add or remove items before finalizing the purchase.

![image](https://github.com/user-attachments/assets/ca217306-e70b-492c-b01a-45104a3e5639)

Free Delivery Threshold:

Order Total & Delivery Fee: If the total value of items in the bag is below $50, users will incur a delivery charge. Also visible on the bag page so users are informed before even reaching checkout page.

Delivery Indicator: The checkout page will clearly show if users are below the $50 threshold, encouraging them to add a bit more to their bag to qualify for free delivery.



Free Delivery: If the total is $50 or more, users will see that delivery is free.

![image](https://github.com/user-attachments/assets/4842d282-33a9-420b-919a-0dd70e353497)

## Key Features of the Subscription Checkout Process:

### Seamless Subscription Signup:

When a user clicks Subscribe on any subscription plan (e.g., meal plans or workout plans), they will be prompted to enter their payment card information to start their subscription.


![image](https://github.com/user-attachments/assets/2eb40352-d3d3-483f-9d67-22fda66742ce)

### Subscription Payments: 

The system is integrated with payment services to ensure users are charged automatically on a monthly basis, and the correct amount is billed each month.

### Product IDs: 

Unique product IDs have been created for each subscription plan to ensure that the system recognizes and processes each subscription correctly, preventing any errors in billing.

### Subscription Management:

Once a user subscribes, they can easily access and manage their active subscriptions from their subscription dashboard.
In the dashboard, users will see their active subscriptions listed along with the details of the subscritiptions.

### Preventing Duplicate Subscriptions:

After subscribing to a particular plan, the system will automatically remove that subscription from the list of available subscriptions. This ensures that users cannot accidentally subscribe to the same plan twice, providing a seamless experience without any confusion.

![image](https://github.com/user-attachments/assets/9c9a9601-72de-46a2-942e-d70334ca6749)

If the user tries to subscribe to a plan they’re already subscribed to, they will receive a notification or a prompt informing them that they are already an active subscriber.
Billing and Payment:

Users will see the price of the subscription clearly displayed during the checkout process, and will be charged the agreed-upon amount automatically every month.
Users can cancel or modify their subscriptions from the subscription dashboard at any time.

## Admin Functionality

Gymstitute provides an intuitive Django Admin Interface that allows administrators to manage products, categories, and subscription plans seamlessly. Admins can easily add, edit, or remove items, as well as manage the various subscription types available to users.

### Managing Products:

Admins can add new products (clothing, equipment, electronics, etc.) directly through the Django admin site.
They can also edit existing products, updating details like price, description, and images, or remove products that are no longer available.

![image](https://github.com/user-attachments/assets/2db8dc49-e582-48ce-bd1e-09f6c4f6b024)

![image](https://github.com/user-attachments/assets/4d5fb16f-5dfa-4329-845a-e9b638d07a3a)


### Managing Categories:

Admins can create and manage product categories (e.g., Gym Equipment, Clothing, Supplements) to help organize the product offerings on the website.
Categories can be added, edited, or deleted to maintain an efficient and user-friendly product catalog.

![image](https://github.com/user-attachments/assets/4ebe36c3-6a5e-48ac-84e2-ebca1c9dc642)

### Managing Subscriptions:

Admins have the ability to create and manage subscription plans (e.g., Meal Plans, Workout Plans).
Admins can define various subscription types (e.g., monthly, quarterly, yearly) and associate them with corresponding pricing and details.
Admins can add new subscription plans, edit or remove existing subscriptions, and ensure that subscriptions are available for users to select.

![image](https://github.com/user-attachments/assets/57d3501f-9505-4e37-806a-87dd35ab01b6)

![image](https://github.com/user-attachments/assets/47c74868-9479-49c6-b6d2-78bf0d3f9ada)

![image](https://github.com/user-attachments/assets/06d4b228-c578-4e59-9eaf-d3d7877cfe1b)

Authentication & Error Handling
Gymstitute employs a secure and user-friendly authentication system powered by Django Allauth, ensuring that user registration, login, and subscription payments are safe and smooth. Additionally, real-time error handling is integrated into the platform, providing clear feedback to users when issues arise during registration, login, or payment processes.

## Authentication:


### Form Error Handling:
#### User Registration & Login:

If a user enters invalid or missing information (such as incorrect credentials or empty fields), clear and real-time error messages will appear on the registration/login form. For example, if a required field is left blank or a password doesn’t meet the required criteria, the form will highlight the error and provide guidance on how to resolve it.

![image](https://github.com/user-attachments/assets/6d4c830b-b45f-42d4-823f-dca66d1569ad)

![image](https://github.com/user-attachments/assets/1fb10d38-122e-4dba-a8c5-72df7177f7d5)

Users are also informed of succcesful logins and logouts.

These error messages are displayed directly above or below the relevant form fields, ensuring users can quickly identify and correct their input.

![image](https://github.com/user-attachments/assets/e00d2f25-2573-4128-8b6b-f87a7e341b03)



## Stripe Card Handler Errors:

### Payment Processing:

When users enter their payment details during the subscription checkout process, Stripe is used as the payment gateway to process card transactions securely.

### Real-Time Error Handling: 

If there’s an issue with the card (e.g., expired card, insufficient funds, or incorrect card number), Stripe will return a specific error message that will be displayed immediately on the checkout page.
Users will be notified with a clear error message (such as "Card declined," "Insufficient funds," or "Invalid card details"), allowing them to quickly correct the issue and try again.
These error messages are designed to be helpful and user-friendly, guiding users toward resolving payment issues without frustration.

![image](https://github.com/user-attachments/assets/8f014f83-4b48-4084-a39b-5841673afa8b)

![image](https://github.com/user-attachments/assets/fdd43664-9894-433f-8088-1b29132037a7)

If users try to pay and do not use a correct country code they wil, get an error dipalyed with a link to view all country codes for assistance in getting the country code right.

![image](https://github.com/user-attachments/assets/7267561c-f7a3-473a-8ee1-236a33aa06b0)

## Custom 404 page

Gymstitute features a custom 404 error page, designed to enhance the user experience by providing a helpful and clear message when users attempt to visit a page that doesn't exist.

![image](https://github.com/user-attachments/assets/d7d8972f-7aee-4b75-9eda-f86944c146b8)



## Benefits of Authentication & Error Handling:

### Enhanced User Experience: 

By providing real-time feedback, users are able to easily correct mistakes or issues, improving their experience with the platform.

### Secure Transactions: 

Stripe’s secure handling of payments ensures that users’ card information is protected throughout the transaction process.



### User Confidence: 

With clear error messages and guidance, users are more confident in completing their registration, login, and subscription payments, knowing that issues will be communicated effectively.

Design Approach
The design of Gymstitute is centered around providing users with a clean, intuitive, and seamless shopping and subscription experience. We have focused on ensuring that the platform is both visually appealing and easy to navigate, while also being fully responsive across all devices.

# GymStitute - Email Authentication and Notifications

This project integrates email notifications for various user actions, including order placements, subscription management, and user sign-up.

## Key Features

### 1. Order Confirmation Emails
   - After a user successfully places an order on the platform, a confirmation email is sent to the email address they provided during checkout.
   - The email contains:
     - A thank-you message.
     - Details of the purchased items.
     - Total order value and any additional relevant information.

### 2. Subscription Management Emails

   - **Subscription Creation**:
   - 
   - After a user subscribes to a ser
   - vice (e.g., a gym membership), they will receive an email confirming their subscription details.
   - **Subscription Cancellation**:
   - If a user cancels their subscription, an email notification is sent confirming the cancellation.

### 3. **User Authentication Emails**

   - **Sign-Up Confirmation**:
   - 
   -  A verification email is sent to users after they sign up. The email contains a confirmation link to verify their email address.
   - **Password Reset**:
   - 
   -  Users can also reset their password if needed via an email with a reset link.

## Design Overview:

### Minimalistic Design: 

The design prioritizes simplicity and clarity. We have kept the interface clean with a minimalistic approach, ensuring that users are not overwhelmed by too many elements at once. Every component is carefully placed to create a visually appealing and functional layout.

### User-Friendly Interface: 

The website is built with user experience in mind. Key features, such as adding products to the shopping bag, checking out, or subscribing to plans, are easily accessible and clearly laid out. The goal is to minimize the number of steps it takes for users to complete tasks.

### Fixed Navigation:

Persistent Navigation: The website features a fixed navigation bar at the top of the page that remains visible as users scroll. This ensures that essential options (like the shopping bag, account login, and navigation links) are always within easy reach.

![image](https://github.com/user-attachments/assets/b69caf25-e4c0-464c-b641-7f0d3bfc1c8f)

### Quick Access: 
Users can quickly navigate between product categories, subscriptions, and their account dashboard without having to scroll back to the top of the page, providing a seamless browsing experience.

### Interactive Elements:

Hover Effects and Button States: Interactive elements, such as buttons, links, and product images, feature clear hover effects to enhance user interaction. Buttons change color or highlight when hovered over to make it easy for users to identify clickable elements.

### Real-Time Feedback: 

Throughout the website, users receive instant feedback when interacting with the platform. For example, when items are added to the shopping bag, the basket icon updates in real time to reflect the number of items and total cost.

### Smooth Transitions: 

Actions like adding products to the bag, navigating through categories, or switching between pages are accompanied by smooth transitions, improving the overall experience.

### Responsive Design:

Mobile and Tablet-Friendly: Gymstitute is fully responsive, meaning the layout automatically adjusts for optimal viewing on devices of all sizes, including smartphones and tablets. Users can browse, shop, and manage subscriptions without any issues, regardless of the device they're using.

### Adaptive Images:

Images, such as product pictures, are dynamically resized to ensure they display correctly on all screen sizes without compromising load times or image quality.

![image](https://github.com/user-attachments/assets/179f8726-7bdb-454f-ae97-2e6fbdbd3a2f)

![image](https://github.com/user-attachments/assets/ad564733-1a50-44a3-ada6-b8477c13aadc)

## Automated Testing

To ensure the reliability and functionality of key features, Gymstitute includes a set of automated tests. These tests were implemented to verify that the core functionalities of the platform, such as subscriptions, checkout, and product views, are working as expected.

## Key Areas Tested:

### Subscription Functionality: 

Basic tests were carried out to confirm that users can subscribe to plans and that subscription details are processed correctly.

### Checkout Process:

Automated tests verify that the checkout process, including item selection, address handling, and payment flow, works without issues.

### Product Views: 

Tests ensure that product pages load correctly, display accurate information, and function as intended.

These automated tests provide confidence that the platform's key features are functioning properly, and they help maintain the quality of the site as new changes are introduced.

The tests are getting 1 failure. An asserrtion error but I have not been able to correct this without breaking other code

![image](https://github.com/user-attachments/assets/d6502c96-f4bf-4184-aaef-6c133038f790)

## Manual Testing

In addition to automated tests, Gymstitute underwent thorough manual testing to ensure all features function as expected across different scenarios. Below is a table outlining the key checks performed during manual testing.

![image](https://github.com/user-attachments/assets/69f0003e-fc25-4593-9217-77afcaa72ef1)

### Performance Testing

The website unfortunetely fails at times with the light house performace . At times it is all above 90 but at other times it can be like below. The indicators of what needs to be chnged is well outside my scope . After extensive research in minimize threadwork and reducing unused CSS and JS without breaking my code I could not get the lighthouse score consistent albeit at times it seems to work fine.One change i did make that vastly improved performance was reducing the background image size. Decision was made to submit as is due to time constraints and knowledge on how to further improve the lighthouse score. 

![image](https://github.com/user-attachments/assets/e2a1cefd-9fcf-48dd-a89e-5f56529c883b)

![image](https://github.com/user-attachments/assets/93ced8bf-dbdd-4542-9e51-bc29820d4a82)


## CSS Validator 

![image](https://github.com/user-attachments/assets/89208bf4-0a0a-4fcd-adac-554f7ebd36d7)

All CSS files passed validator requirements.

HTML Validator was used but errors are shown but more for the reasons of not liking the tag elements included.

![image](https://github.com/user-attachments/assets/ffc61db0-4114-47b3-8b36-c24633bfa9ec)


## Known Bugs and Issues

While Gymstitute is fully functional, there are a few known bugs and issues that are still being addressed. These issues do not impact the overall usability of the website, but they may affect the user experience or site performance in certain situations.

### 1. Subscription Resubscription Issue:

#### Bug: 

When a user cancels a subscription, they are unable to resubscribe immediately. Ideally, users should be able to maintain access to their subscription until the next payment date and then be allowed to subscribe again without issues.

#### Current Status:

This bug is still under investigation, and the goal is to allow users to retain access to their subscription until the next billing cycle before they can resubscribe.
### 2. Performance Issues (Lighthouse Scores):

### Bug: 

The website experiences some performance issues that have been identified through Lighthouse audits, resulting in lower performance scores.

#### Current Status: 

Performance optimization is ongoing, and future updates will focus on improving load times, reducing unnecessary JavaScript execution, and other performance bottlenecks.

### 3. Python Linter Inconsistencies:

#### Bug: 

There are some Flake8 linter inconsistencies that I have not yet been able to fully refactor. Certain parts of the code do not pass the linter without causing code-breaking issues.

#### Current Status: 
These inconsistencies are under review, and I am working on refactoring the code to resolve these issues without affecting the functionality.

### 4. Styling Issues on Certain Screens:

#### Bug: 

Some styling issues occur on certain screens, especially at specific screen sizes or resolutions.

#### Current Status: 

While most screens are properly styled and the site is responsive, occasional layout issues may arise on particular devices. These are minor and do not significantly affect the overall user experience, but ongoing design tweaks are planned to address them.

### Overall Impact:

Despite these issues, the website is fully functional on all screen sizes and provides a smooth experience for users. The core features, such as subscription management, shopping, and checkout, all work as expected, and these issues will be addressed in future updates to improve the site’s performance and usability.

## Future Plans

Gymstitute is continuously evolving to better serve its users and provide even more value. Here are some of the exciting features and improvements planned for the future:

### 1. Expanded Subscription Options:

Run Clubs & Tailored Workout Plans: We plan to introduce run clubs and more tailored workout plans to cater to users with specific fitness goals, such as runners, bodybuilders, or general fitness enthusiasts. This will provide even more variety and personalization to the subscription offerings.

### Customized Meal Plans: 

In addition to general meal plans, we aim to create more specific meal plans tailored to individual dietary preferences, such as keto, vegan, or gluten-free, ensuring all users find a plan that fits their needs.

### 2. User-Generated Product Uploads:

#### Super Users: 
We are working towards allowing super users or trusted community members to add products directly to the website without needing admin access. This will streamline the process of adding new products and offer a wider range of items to choose from.

### 3. Video Content:

#### Free and Paid Video Content:

A major future addition is the introduction of video content on the platform. This will include both free videos (e.g., introductory fitness tutorials, beginner workouts, etc.) and paid content (e.g., premium workout guides, expert fitness tips).

#### Enticing Users to Subscribe:
We plan to offer free initial videos to entice users to sign up for specific plans. This can serve as an engaging way to demonstrate the value of the subscription services and encourage conversions.
These updates are aimed at making Gymstitute even more personalized, engaging, and accessible for all users. The goal is to expand the platform's offerings while maintaining a seamless user experience.

## Marketing

To increase visibility and engagement, Gymstitute has implemented a focused marketing strategy using Facebook to reach and connect with potential customers. This approach aims to build brand awareness, drive traffic to the website, and boost conversions.

### Established Social Presence: 

Gymstitute has a dedicated Facebook business page that serves as a hub for updates, promotions, and community engagement.

![image](https://github.com/user-attachments/assets/be0b3531-ad29-418e-8730-ffc9d7feed3d)


### Product Launch Events: 

We regularly create and post events for product launches and special promotions. These events are designed to generate excitement, encourage attendance, and provide information about new offerings.

![image](https://github.com/user-attachments/assets/2b8a6bda-745e-4033-affe-43683e6f2c8d)

![image](https://github.com/user-attachments/assets/bf507023-bb7e-4179-a0f4-c546778a303f)


### Direct Links to Website:

Posts on our Facebook page include direct links to product pages on the website, making it easy for users to explore and purchase products directly from the platform. This seamless connection from social media to the website aims to improve user engagement and increase conversions.

![image](https://github.com/user-attachments/assets/bd7fa3c8-59e3-4f5c-8d83-7e2a5f2334e0)

![image](https://github.com/user-attachments/assets/039b1f7d-88b6-4cbb-84b9-23962e142b05)



By leveraging Facebook, Gymstitute can reach a wider audience and keep users informed about the latest products, events, and updates. This marketing strategy is a key component of our efforts to build an active and engaged community around the Gymstitute brand.

#### Please be advsied the links on the wesbite will not redirect to the Facebook page as per instruction from the course the page may get deleted by the time of review so the facebook links will just open up the facebook login page.

## Databases and Cloud Hosting

PostgreSQL Database
Gymstitute uses a PostgreSQL database to store essential data, such as user information, product details, order history, and subscription information. PostgreSQL was chosen for its robustness, scalability, and compatibility with Django, providing a reliable relational database that supports the platform's core functionalities. This setup ensures efficient data storage and retrieval, allowing for seamless interactions across the website.


### AWS Cloud Services for Static and Media Files

To manage static assets and media files efficiently, AWS Cloud Services was implemented, providing a secure and scalable solution for hosting Gymstitute’s files.

### S3 Bucket for Storage: 

An AWS S3 bucket was created specifically to host the website’s static files (e.g., CSS, JavaScript) and media files (e.g., product images, user-uploaded images). This setup reduces the load on the main server, ensuring faster load times and a smoother user experience.

#### Security Policies and Permissions:

#### Policies: 
A custom bucket policy was applied to control access, ensuring files are accessible by the website while remaining secure from unauthorized access.
Amazon Resource Name (ARN): An ARN was generated and attached to the policy to establish clear permissions, providing the necessary access rights for the platform to retrieve and display static and media files seamlessly.
Using AWS S3 for static and media file hosting allows Gymstitute to handle larger volumes of data efficiently, optimize load speeds, and provide a scalable solution as the platform grows.

## Agile Development

Gymstitute was developed using an Agile methodology to ensure a flexible, iterative approach to building and refining the platform. This approach allowed for continuous improvement and adaptation based on project requirements and user feedback.

### Kanban Board

#### Task Management:

A Kanban board was used to track progress and manage tasks throughout the development process. Tasks were organized into columns such as “To Do,” “In Progress,” and “Done,” providing a clear, visual representation of the project’s status at any time.

#### Workflow Transparency: 

The Kanban board helped streamline the workflow, allowing team members and stakeholders to monitor progress, prioritize tasks, and address any bottlenecks quickly and efficiently.

### MoSCoW Prioritization
To prioritize tasks and features effectively, the MoSCoW method was applied. This helped ensure that the most critical elements of Gymstitute were developed and delivered on time, while also keeping flexibility for future enhancements.

#### Must-Have: 

Core functionalities such as user registration, product browsing, shopping bag functionality, and the checkout process were identified as Must-Have tasks, critical to the platform’s operation.


![image](https://github.com/user-attachments/assets/a0374cd3-0e8d-4623-94d5-b5abe4f7a15f)


![image](https://github.com/user-attachments/assets/dc483b33-65dc-41d1-83ee-cfa9b4627505)

### Link to the prject board

https://github.com/users/cmoynan/projects/6/views/1

Cloning and Forking the Project from GitHub
To get a copy of the GymStitute project up and running on your local machine, follow these steps:

## Cloning the Repository

Navigate to the GitHub Repository: Go to the GitHub repository page for LocalEatz.

https://github.com/cmoynan/Gymstitute

### Clone the Repository:

Click on the "Code" button on the repository page. Copy the HTTPS or SSH URL provided.

Open Your Terminal:
Open your terminal or command prompt.

Run the Clone Command: git clone https://github.com/your-username/GymStitute.git Replace https://github.com/your-username/Gymstitute.git with the URL you copied.

## Navigate to the Project Directory:

cd GymStitute Forking the Repository

Navigate to the GitHub Repository: Go to the GitHub repository page for GymStitute.

## Fork the Repository:

Click on the "Fork" button in the top-right corner of the repository page. This will create a copy of the repository under your own GitHub account. Clone Your Forked Repository:

Go to your GitHub profile and find the forked repository. Click on the "Code" button on your forked repository page. Copy the HTTPS or SSH URL provided. Open Your Terminal: Open your terminal or command prompt.

### Run the Clone Command:

git clone https://github.com/your-username/Gymstitute.git Replace https://github.com/your-username/GymStitute.git with the URL you copied.

Navigate to the Project Directory: cd LocalEatzApp

## Deployment to Heroku

Gymstitute has been successfully deployed to Heroku to leverage its robust hosting capabilities for Django applications. Here’s an overview of the deployment process and configurations:

### App Creation: 

I created a Heroku app specifically for Gymstitute, choosing an appropriate region to optimize performance for my target audience.

### GitHub Integration:

The Heroku app was linked directly to the Gymstitute GitHub repository, enabling seamless deployment. This integration allows for continuous deployment, ensuring that any updates made to the main branch in GitHub are automatically reflected in the live application.

### Configuration Variables:

Essential configuration variables were added to the Heroku app’s settings to support AWS S3, Stripe, and PostgreSQL. These included:

AWS S3 credentials for static and media file storage, including AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_STORAGE_BUCKET_NAME.
Stripe API keys for secure payment processing, including STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, and STRIPE_WH_SECRET (webhook secret).
DATABASE_URL for PostgreSQL database access, allowing Gymstitute to store and retrieve data reliably.
SECRET_KEY for Django application security, ensuring encrypted sessions and secure data handling.

### Database Setup: 

A PostgreSQL database was provisioned through Heroku’s add-on marketplace, and Heroku generated the DATABASE_URL configuration variable automatically. This database supports all core functionalities of the platform, such as user accounts, product data, and order histories.

#### Static and Media File Storage: 

Static assets and media files were hosted using AWS S3 to enhance load times and reduce the server load. This setup was configured with a custom bucket policy and access permissions using an Amazon Resource Name (ARN), allowing Heroku to retrieve and serve these files seamlessly.

#### Deployment and Testing:

After configuration, the app was deployed to Heroku, with migrations and static file collections executed to finalize setup. The platform was tested in its production environment to ensure all core functionalities, including checkout, subscriptions, and image displays, were working as expected.

Through Heroku's reliable hosting, continuous deployment from GitHub, and integration with PostgreSQL and AWS S3, Gymstitute is now set up to provide users with a seamless, responsive experience in a scalable production environment.

### Heroku deployed app:

https://gymstitute-dd4dc8231064.herokuapp.com/

### Github Repo :

https://github.com/cmoynan/GymStitute










