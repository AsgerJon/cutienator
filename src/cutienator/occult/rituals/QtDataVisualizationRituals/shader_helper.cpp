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
#include "shaderhelper_p.h"
#include <QtOpenGL/QOpenGLShader>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
