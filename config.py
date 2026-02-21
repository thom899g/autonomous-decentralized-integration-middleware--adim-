"""
ADIM Configuration Module
Centralized configuration management for the Autonomous Decentralized Integration Middleware
"""
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional
import logging

@dataclass
class ADIMConfig:
    """Configuration dataclass for ADIM system"""
    
    # Firebase Configuration
    firebase_project_id: str = os.getenv("FIREBASE_PROJECT_ID", "adim-system")
    firebase_credentials_path: str = os.getenv("FIREBASE_CREDENTIALS_PATH", "./credentials/firebase_credentials.json")
    
    # Semantic Layer Configuration
    ontology_base_uri: str = "http://adim.ecosystem/ontology/"
    default_namespace: str = "adim"
    
    # Validation Configuration
    validation_threshold: float = 0.8  # Minimum trust score for connection
    max_validation_nodes: int = 5  # Maximum nodes for decentralized validation
    
    # Dynamic Integration Configuration
    connection_timeout_seconds: int = 30
    max_connection_attempts: int = 3
    heartbeat_interval_seconds: int = 60
    
    # Reinforcement Learning Configuration
    rl_learning_rate: float = 0.01
    rl_discount_factor: float = 0.95
    rl_exploration_rate: float = 0.1
    
    # Logging Configuration
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    @classmethod
    def from_env(cls) -> 'ADIMConfig':
        """Create configuration from environment variables"""
        return cls()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            'firebase_project_id': self.firebase_project_id,
            'ontology_base_uri': self.ontology_base_uri,
            'validation_threshold': self.validation_threshold,
            'max_validation_nodes': self.max_validation_nodes,
            'connection_timeout_seconds': self.connection_timeout_seconds,
            'max_connection_attempts': self.max_connection_attempts,
            'heartbeat_interval_seconds': self.heartbeat_interval_seconds,
            'rl_learning_rate': self.rl_learning_rate,
            'rl_discount_factor': self.rl_discount_factor,
            'rl_exploration_rate': self.rl_exploration_rate
        }

# Global configuration instance
config = ADIMConfig.from_env()

def setup_logging(config: ADIMConfig) -> logging.Logger:
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, config.log_level),
        format=config.log_format
    )
    return logging.getLogger(__name__)