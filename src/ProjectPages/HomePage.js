import aid from '../HackathonPictures/aid.png';
import map from '../map.svg';
import GemLogo from '../hiv.png';
import React,{ useState, useEffect } from 'react';
import Aos from 'aos';
import 'aos/dist/aos.css';

const HomePage = ()=>{
    const [hivStat, setHivStat] = useState("0+");
    const [deathStat, setDeathStat] = useState("0+");

    useEffect(() => {
        const hivInterval = setInterval(() => {
            setHivStat(prevStat => {
                const newValue = parseInt(prevStat) + 1;
                return `${newValue > 25 ? 25 : newValue}+`;
            });
        }, 900); // Interval for updating HIV state

        //STATS COUNTER
        const deathInterval = setInterval(() => {
            setDeathStat(prevStat => {
                const newValue = parseInt(prevStat) + 1;
                return `${newValue > 300 ? 300 : newValue}+`;
            });
        }, 80); // Interval for updating death state

        //LAST CARDS (FOOTER) ANIMATION
        const li = document.querySelectorAll('.Services');
        const observer = new IntersectionObserver((entries)=>{
            entries.forEach((entry)=>{
                if(entry.isIntersecting){
                    entry.target.classList.add("show");
                }else{
                    entry.target.classList.remove('show');
                }
            });
        });
        li.forEach((el)=> observer.observe(el));
        return () => {
            clearInterval(hivInterval); 
            clearInterval(deathInterval);
        };
    }, []);
    //ANIMATION FOR STATS

    useEffect(()=>{
        Aos.init({duration: 2000});
    }, [])
return(
  <div className='HomePage-1st'>
     <div className="main-page">
    {/* ----Header----- */}
     {/* Home page header  */}
        <div className='header'>
            <img src={aid} className='logo'alt='logo'/>
            <h2 className='system-name'>WeCure.</h2>
        </div>
    {/* ---------Content------- */}
    {/* Content Display information */}
    <div className='pageContent'>
        <p>
        At WeCure, <br/>we're on a mission to combat HIV and empower individuals to take control of their health and well-being.
        <br/> With our innovative platform, powered by AI and advanced technology, <br/>we offer personalized healthcare services and support to users worldwide.
        </p>
        <h4 className='slogan'>Taking care of you is taking care of your loved ones.</h4>
        <button>Sign Up</button>
    </div>
   </div>

   {/* ----------------------------------------------------------------------------------------------------- */}
        {/* ----Body--- */}
        <div className='pageBody'>
            {/* Body of Web Page */}
            {/* ----Cards-- */}
            <div className='cards'>
                {/* Stats in Cards */}
                <div className='Card-1'>
                    <h1 data-aos="zoom-in">{hivStat}</h1>
                    <h3>Million people in Africa are living with HIV.</h3>
                </div>
                <div className='Card-2'>
                    <h1 data-aos="zoom-in">{deathStat}</h1>
                    <h3>Thousand people died from HIV illness in 2022.</h3>
                </div>
            </div>
            {/* ---------World Map--------- */}
            <div className='Hiv-history'>
                {/* //history Summary */}
                <h1>Understanding HIV: Causes & Damages</h1>
                <p data-aos="fade-in">The <b>Human immunodeficiency virus (HIV)</b> targets cells in the immune system - the body's defence against illness - 
                and weakness the body's ability to fight against infections and some types of cancer. The virus destroys white blood cells in the immune system
                called CD4 cells and replicates itself inside these cells.</p>
                <p data-aos="fade-in">As the virus destroys and impairs the function  of immume cells, infected individuals gradually become immunodeficient. The body becomes increasingly unable to fight infections and disease and vulnerable to opportunistic infections and cancers. Immune funciton is typically measured by CD4 cell count.</p>
                <img src={map} alt='World Map' className='map'/>
                <h6>(113 Million people living with HIV worldwide)</h6>
            </div>
            {/* --------WHY WeCure */}
            <div className='WeCure'>
            {/* WeCure description */} 
                <h1>Choosing <b>WeCure</b>  :</h1>
                <p data-aos="fade-up">At <b>WeCure</b> revolutionize healthcare delivery by integrating cutting-edge technologies such as artificial intelligence,
                our system, you can receive accurate diagnoses, personalized treatment recommendations, and access to healthcare resources in multiple languages such as:<br/>
                <ul className='languages'>
                    <li>English</li>
                    <li>IsiZulu</li>
                    <li>Afrikaans</li>
                    <li>IsiXhosa</li>
                </ul>
                <br/>
                for a seamless user experience.
                </p>
                {/* -----KEY FECTURES----- */}
                <h2>How It Works:</h2>
                <ul className='Services'>
                    <li>Our AI-powered system prompts you to articulate any symptoms you're experiencing through our intuitive chatbot interface</li>
                    <li>Utilizing WeCure ML, you can effortlessly upload images of any physical symptoms you observe, ensuring comprehensive monitoring.</li>
                    <li>Cutting-edge AI algorithms meticulously analyze your symptoms, offering insightful diagnoses and tailored recommendations for your well-being.</li>
                </ul>
                <h2>If found Positve:</h2>
                    <ul className='Services'>
                        <li>We accompany you throughout your health journey, providing personalized daily activity recommendations and timely medication notifications.</li>
                        <li>Our advanced system seamlessly generates doctor's letters for scheduling check-up appointments at nearby hospitals in your locality.</li>
                        <li>Gain invaluable insights and knowledge to make well-informed decisions regarding your health and overall well-being.</li>
                    </ul>
            </div>
            {/* ----Footer------- */}
            {/* Home Page Footer*/}
            <div className='Footer'>
                <p>Our mission is to empower individuals to take control of their health and well-being through accessible, personalized, and innovative healthcare solutions.</p>
                <p>We are committed to leveraging technology to improve healthcare outcomes and enhance the lives of users worldwide.</p>
                <img src={GemLogo} alt='Logo' className='GemLogo'/>
                <p>www.WeCure.org.za</p>
            </div>
        </div>
  </div>
)
}

export default HomePage;