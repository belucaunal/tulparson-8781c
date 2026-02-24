#!/usr/bin/env python3
"""
Backend API Testing Script for Tulpar Kurye
Tests all backend endpoints to verify functionality
"""

import requests
import json
from datetime import datetime
import os
import sys

# Get backend URL from environment (same as frontend uses)
BACKEND_URL = "https://district-kurye.preview.emergentagent.com"
API_BASE = f"{BACKEND_URL}/api"

def test_health_endpoint():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check Endpoint ===")
    
    try:
        url = f"{API_BASE}/health"
        print(f"Testing: GET {url}")
        
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            # Verify response structure
            if "status" in data and "timestamp" in data:
                if data["status"] == "healthy":
                    print("✅ Health check endpoint working correctly")
                    return True
                else:
                    print(f"❌ Health check status not 'healthy': {data['status']}")
                    return False
            else:
                print("❌ Health check response missing required fields")
                return False
        else:
            print(f"❌ Health check failed with status {response.status_code}")
            if response.text:
                print(f"Response body: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check request failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Health check test failed with error: {e}")
        return False

def test_root_endpoint():
    """Test the root API endpoint"""
    print("\n=== Testing Root API Endpoint ===")
    
    try:
        url = f"{API_BASE}/"
        print(f"Testing: GET {url}")
        
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            print("✅ Root API endpoint working correctly")
            return True
        else:
            print(f"❌ Root API failed with status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Root API request failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Root API test failed with error: {e}")
        return False

def main():
    """Run all backend tests"""
    print("🚀 Starting Backend API Tests for Tulpar Kurye")
    print(f"Backend URL: {BACKEND_URL}")
    print(f"API Base URL: {API_BASE}")
    
    tests_passed = 0
    tests_total = 2
    
    # Test health endpoint
    if test_health_endpoint():
        tests_passed += 1
    
    # Test root endpoint  
    if test_root_endpoint():
        tests_passed += 1
    
    print(f"\n{'='*50}")
    print(f"BACKEND TEST RESULTS: {tests_passed}/{tests_total} tests passed")
    
    if tests_passed == tests_total:
        print("✅ All backend tests PASSED")
        return True
    else:
        print("❌ Some backend tests FAILED")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)