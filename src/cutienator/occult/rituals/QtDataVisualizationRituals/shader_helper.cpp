//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/shaderhelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/shaderhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtOpenGL/QOpenGLShader>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 10, as local:shaderhelper.cpp:discardDebugMsgs
inline void discardDebugMsgs(QtMsgType type, const QMessageLogContext &context, const QString &msg)
{
    Q_UNUSED(type);
    Q_UNUSED(context);
    Q_UNUSED(msg);
    // Used to discard warnings generated during shader test compilation
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 18, as _ZN12ShaderHelperC1EP7QObjectRK7QStringS4_S4_S4_
inline ShaderHelper::ShaderHelper(QObject *parent,
                           const QString &vertexShader,
                           const QString &fragmentShader,
                           const QString &texture,
                           const QString &depthTexture)
    : m_caller(parent),
      m_program(0),
      m_vertexShaderFile(vertexShader),
      m_fragmentShaderFile(fragmentShader),
      m_textureFile(texture),
      m_depthTextureFile(depthTexture),
      m_positionAttr(0),
      m_uvAttr(0),
      m_normalAttr(0),
      m_colorUniform(0),
      m_viewMatrixUniform(0),
      m_modelMatrixUniform(0),
      m_invTransModelMatrixUniform(0),
      m_depthMatrixUniform(0),
      m_mvpMatrixUniform(0),
      m_lightPositionUniform(0),
      m_lightStrengthUniform(0),
      m_ambientStrengthUniform(0),
      m_shadowQualityUniform(0),
      m_textureUniform(0),
      m_shadowUniform(0),
      m_gradientMinUniform(0),
      m_gradientHeightUniform(0),
      m_lightColorUniform(0),
      m_volumeSliceIndicesUniform(0),
      m_colorIndexUniform(0),
      m_cameraPositionRelativeToModelUniform(0),
      m_color8BitUniform(0),
      m_textureDimensionsUniform(0),
      m_sampleCountUniform(0),
      m_alphaMultiplierUniform(0),
      m_preserveOpacityUniform(0),
      m_minBoundsUniform(0),
      m_maxBoundsUniform(0),
      m_sliceFrameWidthUniform(0),
      m_initialized(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 62, as _ZN12ShaderHelperD1Ev
inline ShaderHelper::~ShaderHelper()
{
    delete m_program;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 67, as _ZN12ShaderHelper10setShadersERK7QStringS2_
inline void ShaderHelper::setShaders(const QString &vertexShader,
                              const QString &fragmentShader)
{
    m_vertexShaderFile = vertexShader;
    m_fragmentShaderFile = fragmentShader;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 74, as _ZN12ShaderHelper11setTexturesERK7QStringS2_
inline void ShaderHelper::setTextures(const QString &texture,
                               const QString &depthTexture)
{
    m_textureFile = texture;
    m_depthTextureFile = depthTexture;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 81, as _ZN12ShaderHelper10initializeEv
inline void ShaderHelper::initialize()
{
    if (m_program)
        delete m_program;
    m_program = new QOpenGLShaderProgram(m_caller);
    if (!m_program->addShaderFromSourceFile(QOpenGLShader::Vertex, m_vertexShaderFile))
        qFatal("Compiling Vertex shader failed");
    if (!m_program->addShaderFromSourceFile(QOpenGLShader::Fragment, m_fragmentShaderFile))
        qFatal("Compiling Fragment shader failed");

    if (!m_program->link()) {
        qWarning() << "Unable to link shader program:" <<
                      m_vertexShaderFile << m_fragmentShaderFile;
        return;
    }

    m_positionAttr = m_program->attributeLocation("vertexPosition_mdl");
    m_normalAttr = m_program->attributeLocation("vertexNormal_mdl");
    m_uvAttr = m_program->attributeLocation("vertexUV");

    m_mvpMatrixUniform = m_program->uniformLocation("MVP");
    m_viewMatrixUniform = m_program->uniformLocation("V");
    m_modelMatrixUniform = m_program->uniformLocation("M");
    m_invTransModelMatrixUniform = m_program->uniformLocation("itM");
    m_depthMatrixUniform = m_program->uniformLocation("depthMVP");
    m_lightPositionUniform = m_program->uniformLocation("lightPosition_wrld");
    m_lightStrengthUniform = m_program->uniformLocation("lightStrength");
    m_ambientStrengthUniform = m_program->uniformLocation("ambientStrength");
    m_shadowQualityUniform = m_program->uniformLocation("shadowQuality");
    m_colorUniform = m_program->uniformLocation("color_mdl");
    m_textureUniform = m_program->uniformLocation("textureSampler");
    m_shadowUniform = m_program->uniformLocation("shadowMap");
    m_gradientMinUniform = m_program->uniformLocation("gradMin");
    m_gradientHeightUniform = m_program->uniformLocation("gradHeight");
    m_lightColorUniform = m_program->uniformLocation("lightColor");
    m_volumeSliceIndicesUniform = m_program->uniformLocation("volumeSliceIndices");
    m_colorIndexUniform = m_program->uniformLocation("colorIndex");
    m_cameraPositionRelativeToModelUniform = m_program->uniformLocation("cameraPositionRelativeToModel");
    m_color8BitUniform = m_program->uniformLocation("color8Bit");
    m_textureDimensionsUniform = m_program->uniformLocation("textureDimensions");
    m_sampleCountUniform = m_program->uniformLocation("sampleCount");
    m_alphaMultiplierUniform = m_program->uniformLocation("alphaMultiplier");
    m_preserveOpacityUniform = m_program->uniformLocation("preserveOpacity");
    m_minBoundsUniform = m_program->uniformLocation("minBounds");
    m_maxBoundsUniform = m_program->uniformLocation("maxBounds");
    m_sliceFrameWidthUniform = m_program->uniformLocation("sliceFrameWidth");
    m_initialized = true;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 130, as _ZN12ShaderHelper11testCompileEv
inline bool ShaderHelper::testCompile()
{
    bool result = true;

    // Discard warnings, we only need the result
    QtMessageHandler handler = qInstallMessageHandler(discardDebugMsgs);
    if (m_program)
        delete m_program;
    m_program = new QOpenGLShaderProgram();
    if (!m_program->addShaderFromSourceFile(QOpenGLShader::Vertex, m_vertexShaderFile))
        result = false;
    if (!m_program->addShaderFromSourceFile(QOpenGLShader::Fragment, m_fragmentShaderFile))
        result = false;

    // Restore actual message handler
    qInstallMessageHandler(handler);
    return result;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 149, as _ZN12ShaderHelper4bindEv
inline void ShaderHelper::bind()
{
    m_program->bind();
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 154, as _ZN12ShaderHelper7releaseEv
inline void ShaderHelper::release()
{
    m_program->release();
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 159, as _ZN12ShaderHelper15setUniformValueEiRK9QVector2D
inline void ShaderHelper::setUniformValue(GLint uniform, const QVector2D &value)
{
    m_program->setUniformValue(uniform, value);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 164, as _ZN12ShaderHelper15setUniformValueEiRK9QVector3D
inline void ShaderHelper::setUniformValue(GLint uniform, const QVector3D &value)
{
    m_program->setUniformValue(uniform, value);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 169, as _ZN12ShaderHelper15setUniformValueEiRK9QVector4D
inline void ShaderHelper::setUniformValue(GLint uniform, const QVector4D &value)
{
    m_program->setUniformValue(uniform, value);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 174, as _ZN12ShaderHelper15setUniformValueEiRK10QMatrix4x4
inline void ShaderHelper::setUniformValue(GLint uniform, const QMatrix4x4 &value)
{
    m_program->setUniformValue(uniform, value);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 179, as _ZN12ShaderHelper15setUniformValueEif
inline void ShaderHelper::setUniformValue(GLint uniform, GLfloat value)
{
    m_program->setUniformValue(uniform, value);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 184, as _ZN12ShaderHelper15setUniformValueEii
inline void ShaderHelper::setUniformValue(GLint uniform, GLint value)
{
    m_program->setUniformValue(uniform, value);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 189, as _ZN12ShaderHelper20setUniformValueArrayEiPK9QVector4Di
inline void ShaderHelper::setUniformValueArray(GLint uniform, const QVector4D *values, int count)
{
    m_program->setUniformValueArray(uniform, values, count);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 194, as _ZN12ShaderHelper3MVPEv
inline GLint ShaderHelper::MVP()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_mvpMatrixUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 201, as _ZN12ShaderHelper4viewEv
inline GLint ShaderHelper::view()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_viewMatrixUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 208, as _ZN12ShaderHelper5modelEv
inline GLint ShaderHelper::model()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_modelMatrixUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 215, as _ZN12ShaderHelper6nModelEv
inline GLint ShaderHelper::nModel()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_invTransModelMatrixUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 222, as _ZN12ShaderHelper5depthEv
inline GLint ShaderHelper::depth()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_depthMatrixUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 229, as _ZN12ShaderHelper6lightPEv
inline GLint ShaderHelper::lightP()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_lightPositionUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 236, as _ZN12ShaderHelper6lightSEv
inline GLint ShaderHelper::lightS()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_lightStrengthUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 243, as _ZN12ShaderHelper8ambientSEv
inline GLint ShaderHelper::ambientS()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_ambientStrengthUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 250, as _ZN12ShaderHelper7shadowQEv
inline GLint ShaderHelper::shadowQ()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_shadowQualityUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 257, as _ZN12ShaderHelper5colorEv
inline GLint ShaderHelper::color()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_colorUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 264, as _ZN12ShaderHelper7textureEv
inline GLint ShaderHelper::texture()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_textureUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 271, as _ZN12ShaderHelper6shadowEv
inline GLint ShaderHelper::shadow()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_shadowUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 278, as _ZN12ShaderHelper11gradientMinEv
inline GLint ShaderHelper::gradientMin()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_gradientMinUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 285, as _ZN12ShaderHelper14gradientHeightEv
inline GLint ShaderHelper::gradientHeight()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_gradientHeightUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 292, as _ZN12ShaderHelper10lightColorEv
inline GLint ShaderHelper::lightColor()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_lightColorUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 299, as _ZN12ShaderHelper18volumeSliceIndicesEv
inline GLint ShaderHelper::volumeSliceIndices()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_volumeSliceIndicesUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 306, as _ZN12ShaderHelper10colorIndexEv
inline GLint ShaderHelper::colorIndex()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_colorIndexUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 313, as _ZN12ShaderHelper29cameraPositionRelativeToModelEv
inline GLint ShaderHelper::cameraPositionRelativeToModel()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_cameraPositionRelativeToModelUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 320, as _ZN12ShaderHelper9color8BitEv
inline GLint ShaderHelper::color8Bit()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_color8BitUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 327, as _ZN12ShaderHelper17textureDimensionsEv
inline GLint ShaderHelper::textureDimensions()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_textureDimensionsUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 334, as _ZN12ShaderHelper11sampleCountEv
inline GLint ShaderHelper::sampleCount()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_sampleCountUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 341, as _ZN12ShaderHelper15alphaMultiplierEv
inline GLint ShaderHelper::alphaMultiplier()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_alphaMultiplierUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 348, as _ZN12ShaderHelper15preserveOpacityEv
inline GLint ShaderHelper::preserveOpacity()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_preserveOpacityUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 355, as _ZN12ShaderHelper9maxBoundsEv
inline GLint ShaderHelper::maxBounds()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_maxBoundsUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 362, as _ZN12ShaderHelper9minBoundsEv
inline GLint ShaderHelper::minBounds()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_minBoundsUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 369, as _ZN12ShaderHelper15sliceFrameWidthEv
inline GLint ShaderHelper::sliceFrameWidth()
{

    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_sliceFrameWidthUniform;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 377, as _ZN12ShaderHelper6posAttEv
inline GLint ShaderHelper::posAtt()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_positionAttr;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 384, as _ZN12ShaderHelper5uvAttEv
inline GLint ShaderHelper::uvAtt()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_uvAttr;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 391, as _ZN12ShaderHelper9normalAttEv
inline GLint ShaderHelper::normalAtt()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_normalAttr;
}
//  -----------------------------------------------------------------------

//  ShaderHelper::ShaderHelper(QObject *parent, const QString &vertexShader,
//      const QString &fragmentShader, const QString &texture, const QString
//      &depthTexture)
extern "C" Q_DECL_EXPORT
ShaderHelper *ritual_ZN12ShaderHelperC1EP7QObjectRK7QStringS4_S4_S4_(
    QObject *parent,
    const QString *vertexShader,
    const QString *fragmentShader,
    const QString *texture,
    const QString *depthTexture) {
  return new ShaderHelper(
      parent,
      *vertexShader,
      *fragmentShader,
      *texture,
      *depthTexture);
}

//  ShaderHelper::~ShaderHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelperD1Ev(ShaderHelper *self) {
  delete self;
}

//  void ShaderHelper::setShaders(const QString &vertexShader, const QString
//      &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper10setShadersERK7QStringS2_(
    ShaderHelper *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->setShaders(*vertexShader, *fragmentShader);
}

//  void ShaderHelper::setTextures(const QString &texture, const QString
//      &depthTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper11setTexturesERK7QStringS2_(
    ShaderHelper *self,
    const QString *texture,
    const QString *depthTexture) {
  self->setTextures(*texture, *depthTexture);
}

//  void ShaderHelper::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper10initializeEv(ShaderHelper *self) {
  self->initialize();
}

//  bool ShaderHelper::testCompile()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12ShaderHelper11testCompileEv(ShaderHelper *self) {
  return self->testCompile();
}

//  void ShaderHelper::bind()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper4bindEv(ShaderHelper *self) {
  self->bind();
}

//  void ShaderHelper::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper7releaseEv(ShaderHelper *self) {
  self->release();
}

//  void ShaderHelper::setUniformValue(GLint uniform, const QVector2D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper15setUniformValueEiRK9QVector2D(
    ShaderHelper *self,
    GLint uniform,
    const QVector2D *value) {
  self->setUniformValue(uniform, *value);
}

//  void ShaderHelper::setUniformValue(GLint uniform, const QVector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper15setUniformValueEiRK9QVector3D(
    ShaderHelper *self,
    GLint uniform,
    const QVector3D *value) {
  self->setUniformValue(uniform, *value);
}

//  void ShaderHelper::setUniformValue(GLint uniform, const QVector4D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper15setUniformValueEiRK9QVector4D(
    ShaderHelper *self,
    GLint uniform,
    const QVector4D *value) {
  self->setUniformValue(uniform, *value);
}

//  void ShaderHelper::setUniformValue(GLint uniform, const QMatrix4x4
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper15setUniformValueEiRK10QMatrix4x4(
    ShaderHelper *self,
    GLint uniform,
    const QMatrix4x4 *value) {
  self->setUniformValue(uniform, *value);
}

//  void ShaderHelper::setUniformValue(GLint uniform, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper15setUniformValueEif(
    ShaderHelper *self,
    GLint uniform,
    GLfloat value) {
  self->setUniformValue(uniform, value);
}

//  void ShaderHelper::setUniformValue(GLint uniform, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper15setUniformValueEii(
    ShaderHelper *self,
    GLint uniform,
    GLint value) {
  self->setUniformValue(uniform, value);
}

//  void ShaderHelper::setUniformValueArray(GLint uniform, const QVector4D
//      *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ShaderHelper20setUniformValueArrayEiPK9QVector4Di(
    ShaderHelper *self,
    GLint uniform,
    const QVector4D *values,
    int count) {
  self->setUniformValueArray(uniform, values, count);
}

//  GLint ShaderHelper::MVP()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper3MVPEv(ShaderHelper *self) {
  return self->MVP();
}

//  GLint ShaderHelper::view()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper4viewEv(ShaderHelper *self) {
  return self->view();
}

//  GLint ShaderHelper::model()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper5modelEv(ShaderHelper *self) {
  return self->model();
}

//  GLint ShaderHelper::nModel()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper6nModelEv(ShaderHelper *self) {
  return self->nModel();
}

//  GLint ShaderHelper::depth()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper5depthEv(ShaderHelper *self) {
  return self->depth();
}

//  GLint ShaderHelper::lightP()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper6lightPEv(ShaderHelper *self) {
  return self->lightP();
}

//  GLint ShaderHelper::lightS()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper6lightSEv(ShaderHelper *self) {
  return self->lightS();
}

//  GLint ShaderHelper::ambientS()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper8ambientSEv(ShaderHelper *self) {
  return self->ambientS();
}

//  GLint ShaderHelper::shadowQ()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper7shadowQEv(ShaderHelper *self) {
  return self->shadowQ();
}

//  GLint ShaderHelper::color()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper5colorEv(ShaderHelper *self) {
  return self->color();
}

//  GLint ShaderHelper::texture()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper7textureEv(ShaderHelper *self) {
  return self->texture();
}

//  GLint ShaderHelper::shadow()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper6shadowEv(ShaderHelper *self) {
  return self->shadow();
}

//  GLint ShaderHelper::gradientMin()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper11gradientMinEv(ShaderHelper *self) {
  return self->gradientMin();
}

//  GLint ShaderHelper::gradientHeight()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper14gradientHeightEv(ShaderHelper *self) {
  return self->gradientHeight();
}

//  GLint ShaderHelper::lightColor()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper10lightColorEv(ShaderHelper *self) {
  return self->lightColor();
}

//  GLint ShaderHelper::volumeSliceIndices()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper18volumeSliceIndicesEv(ShaderHelper *self) {
  return self->volumeSliceIndices();
}

//  GLint ShaderHelper::colorIndex()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper10colorIndexEv(ShaderHelper *self) {
  return self->colorIndex();
}

//  GLint ShaderHelper::cameraPositionRelativeToModel()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper29cameraPositionRelativeToModelEv(
    ShaderHelper *self) {
  return self->cameraPositionRelativeToModel();
}

//  GLint ShaderHelper::color8Bit()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper9color8BitEv(ShaderHelper *self) {
  return self->color8Bit();
}

//  GLint ShaderHelper::textureDimensions()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper17textureDimensionsEv(ShaderHelper *self) {
  return self->textureDimensions();
}

//  GLint ShaderHelper::sampleCount()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper11sampleCountEv(ShaderHelper *self) {
  return self->sampleCount();
}

//  GLint ShaderHelper::alphaMultiplier()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper15alphaMultiplierEv(ShaderHelper *self) {
  return self->alphaMultiplier();
}

//  GLint ShaderHelper::preserveOpacity()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper15preserveOpacityEv(ShaderHelper *self) {
  return self->preserveOpacity();
}

//  GLint ShaderHelper::maxBounds()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper9maxBoundsEv(ShaderHelper *self) {
  return self->maxBounds();
}

//  GLint ShaderHelper::minBounds()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper9minBoundsEv(ShaderHelper *self) {
  return self->minBounds();
}

//  GLint ShaderHelper::sliceFrameWidth()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper15sliceFrameWidthEv(ShaderHelper *self) {
  return self->sliceFrameWidth();
}

//  GLint ShaderHelper::posAtt()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper6posAttEv(ShaderHelper *self) {
  return self->posAtt();
}

//  GLint ShaderHelper::uvAtt()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper5uvAttEv(ShaderHelper *self) {
  return self->uvAtt();
}

//  GLint ShaderHelper::normalAtt()
extern "C" Q_DECL_EXPORT
GLint ritual_ZN12ShaderHelper9normalAttEv(ShaderHelper *self) {
  return self->normalAtt();
}
