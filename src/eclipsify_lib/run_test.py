runTestTemplate=R'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<launchConfiguration type="org.eclipse.cdt.testsrunner.launch.CTestsRunner">
<intAttribute key="org.eclipse.cdt.launch.ATTR_BUILD_BEFORE_LAUNCH_ATTR" value="2"/>
<stringAttribute key="org.eclipse.cdt.launch.COREFILE_PATH" value=""/>
<stringAttribute key="org.eclipse.cdt.launch.PROGRAM_ARGUMENTS" value="&quot;{1}&quot;"/>
<stringAttribute key="org.eclipse.cdt.launch.PROGRAM_NAME" value="{2}"/>
<stringAttribute key="org.eclipse.cdt.launch.PROJECT_ATTR" value="{0}"/>
<booleanAttribute key="org.eclipse.cdt.launch.PROJECT_BUILD_CONFIG_AUTO_ATTR" value="false"/>
<stringAttribute key="org.eclipse.cdt.launch.PROJECT_BUILD_CONFIG_ID_ATTR" value="cdt.managedbuild.toolchain.gnu.macosx.base.205247326.2127756105"/>
<booleanAttribute key="org.eclipse.cdt.launch.use_terminal" value="true"/>
<stringAttribute key="org.eclipse.cdt.testsrunner.launch.TESTS_RUNNER" value="org.eclipse.cdt.testsrunner.gtest"/>
<listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_PATHS">
<listEntry value="/{0}"/>
</listAttribute>
<listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_TYPES">
<listEntry value="4"/>
</listAttribute>
<stringAttribute key="process_factory_id" value="org.eclipse.cdt.testsrunner.TestingProcessFactory"/>
</launchConfiguration>
'''

def runTest(packageName, fullPathToTestBinary, fullPathToEnv):
    return runTestTemplate.format(packageName, fullPathToTestBinary, fullPathToEnv)
