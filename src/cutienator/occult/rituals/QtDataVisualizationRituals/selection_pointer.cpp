//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/selectionpointer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/selectionpointer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtOpenGL/QOpenGLShader>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#include <QtDataVisualization/private/drawer_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/surfaceobject_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/scatterpointbufferhelper_p.h>
#include <QtGui/QMatrix4x4>
#include <QtGui/qquaternion.h>
#include <QtCore/qmath.h>
#include <QtDataVisualization/private/selectionpointer_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/objecthelper_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/q3dcamera_p.h>
#include <QtDataVisualization/private/utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 37, as _ZN13TextureHelperD1Ev
inline TextureHelper::~TextureHelper()
{
#if !QT_CONFIG(opengles2)
    delete m_openGlFunctions_2_1;
#endif
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 407, as _ZN6Drawer17generateLabelItemER9LabelItemRK7QStringi
inline void Drawer::generateLabelItem(LabelItem &item, const QString &text, int widestLabel)
{
    initializeOpenGL();

    item.clear();

    if (!text.isEmpty()) {
        // Create labels
        // Print label into a QImage using QPainter
        QImage label = Utils::printTextToImage(m_theme->font(),
                                               text,
                                               m_theme->labelBackgroundColor(),
                                               m_theme->labelTextColor(),
                                               m_theme->isLabelBackgroundEnabled(),
                                               m_theme->isLabelBorderEnabled(),
                                               widestLabel);

        // Set label size
        item.setSize(label.size());
        // Insert text texture into label (also deletes the old texture)
        item.setTextureId(m_textureHelper->create2DTexture(label, true, true));
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 68, as _ZNK6Drawer5themeEv
inline Q3DTheme *Drawer::theme() const
{
    return m_theme;
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 54, as _ZN6Drawer16initializeOpenGLEv
inline void Drawer::initializeOpenGL()
{
    initializeOpenGLFunctions();
    if (!m_textureHelper)
        m_textureHelper = new TextureHelper();
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 44, as _ZN13TextureHelper15create2DTextureERK6QImagebbbb
inline GLuint TextureHelper::create2DTexture(const QImage &image, bool useTrilinearFiltering,
                                      bool convert, bool smoothScale, bool clampY)
{
    if (image.isNull())
        return 0;

    QImage texImage = image;

    if (Utils::isOpenGLES()) {
        GLuint imageWidth = Utils::getNearestPowerOfTwo(image.width());
        GLuint imageHeight = Utils::getNearestPowerOfTwo(image.height());
        if (smoothScale) {
            texImage = image.scaled(imageWidth, imageHeight, Qt::IgnoreAspectRatio,
                                    Qt::SmoothTransformation);
        } else {
            texImage = image.scaled(imageWidth, imageHeight, Qt::IgnoreAspectRatio);
        }
    }

    GLuint textureId;
    glGenTextures(1, &textureId);
    glBindTexture(GL_TEXTURE_2D, textureId);
    if (convert)
        texImage = convertToGLFormat(texImage);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texImage.width(), texImage.height(),
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texImage.bits());
    if (smoothScale)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    else
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    if (useTrilinearFiltering) {
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
        glGenerateMipmap(GL_TEXTURE_2D);
    } else {
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    }
    if (clampY)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glBindTexture(GL_TEXTURE_2D, 0);

    return textureId;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 33, as _ZN16SelectionPointerD1Ev
inline SelectionPointer::~SelectionPointer()
{
    delete m_labelShader;
    delete m_pointShader;
    delete m_textureHelper;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 208, as _ZN16SelectionPointer11setPositionERK9QVector3D
inline void SelectionPointer::setPosition(const QVector3D &position)
{
    m_position = position;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 237, as _ZN16SelectionPointer16setPointerObjectEP12ObjectHelper
inline void SelectionPointer::setPointerObject(ObjectHelper *object)
{
    m_pointObj = object;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 242, as _ZN16SelectionPointer14setLabelObjectEP12ObjectHelper
inline void SelectionPointer::setLabelObject(ObjectHelper *object)
{
    m_labelObj = object;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 253, as _ZN16SelectionPointer18updateBoundingRectERK5QRect
inline void SelectionPointer::updateBoundingRect(const QRect &rect)
{
    m_mainViewPort = rect;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 50, as _ZN16SelectionPointer11updateSceneEP8Q3DScene
inline void SelectionPointer::updateScene(Q3DScene *scene)
{
    m_cachedScene = scene;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 213, as _ZN16SelectionPointer15updateSliceDataEbf
inline void SelectionPointer::updateSliceData(bool sliceActivated, GLfloat autoScaleAdjustment)
{
    m_cachedIsSlicingActivated = sliceActivated;
    m_autoScaleAdjustment = autoScaleAdjustment;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 219, as _ZN16SelectionPointer17setHighlightColorERK9QVector4D
inline void SelectionPointer::setHighlightColor(const QVector4D &colorVector)
{
    m_highlightColor = colorVector;
}

//  from ../qtdatavis3d/src/datavisualization/engine/selectionpointer.cpp, line 224, as _ZN16SelectionPointer11setRotationERK11QQuaternion
inline void SelectionPointer::setRotation(const QQuaternion &rotation)
{
    m_rotation = rotation;
}
//  -----------------------------------------------------------------------

//  A SelectionPointer that Python can take functions over in. Every SelectionPointer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSelectionPointerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSelectionPointerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSelectionPointerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSelectionPointerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSelectionPointerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSelectionPointerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSelectionPointerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSelectionPointer : public SelectionPointer {
public:
  using SelectionPointer::SelectionPointer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteSelectionPointerCall0 call = reinterpret_cast<CuteSelectionPointerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteSelectionPointerCall1 call = reinterpret_cast<CuteSelectionPointerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteSelectionPointerCall2 call = reinterpret_cast<CuteSelectionPointerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteSelectionPointerCall3 call = reinterpret_cast<CuteSelectionPointerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteSelectionPointerCall4 call = reinterpret_cast<CuteSelectionPointerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteSelectionPointerCall5 call = reinterpret_cast<CuteSelectionPointerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteSelectionPointerCall6 call = reinterpret_cast<CuteSelectionPointerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *SelectionPointer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16SelectionPointer10metaObjectEv(
    const SelectionPointer *self) {
  return self->metaObject();
}

//  SelectionPointer::~SelectionPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointerD1Ev(SelectionPointer *self) {
  delete self;
}

//  void SelectionPointer::setPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer11setPositionERK9QVector3D(
    SelectionPointer *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  void SelectionPointer::setPointerObject(ObjectHelper *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer16setPointerObjectEP12ObjectHelper(
    SelectionPointer *self,
    ObjectHelper *object) {
  self->setPointerObject(object);
}

//  void SelectionPointer::setLabelObject(ObjectHelper *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer14setLabelObjectEP12ObjectHelper(
    SelectionPointer *self,
    ObjectHelper *object) {
  self->setLabelObject(object);
}

//  void SelectionPointer::updateBoundingRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer18updateBoundingRectERK5QRect(
    SelectionPointer *self,
    const QRect *rect) {
  self->updateBoundingRect(*rect);
}

//  void SelectionPointer::updateScene(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer11updateSceneEP8Q3DScene(
    SelectionPointer *self,
    Q3DScene *scene) {
  self->updateScene(scene);
}

//  void SelectionPointer::updateSliceData(bool sliceActivated, GLfloat
//      autoScaleAdjustment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer15updateSliceDataEbf(
    SelectionPointer *self,
    bool sliceActivated,
    GLfloat autoScaleAdjustment) {
  self->updateSliceData(sliceActivated, autoScaleAdjustment);
}

//  void SelectionPointer::setHighlightColor(const QVector4D &colorVector)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer17setHighlightColorERK9QVector4D(
    SelectionPointer *self,
    const QVector4D *colorVector) {
  self->setHighlightColor(*colorVector);
}

//  void SelectionPointer::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SelectionPointer11setRotationERK11QQuaternion(
    SelectionPointer *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}

//  SelectionPointer as the QOpenGLFunctions it is built on
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_cast_SelectionPointer_QOpenGLFunctions(
    SelectionPointer *self) {
  return static_cast<QOpenGLFunctions *>(self);
}

//  a Python function taken by a CuteSelectionPointer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SelectionPointer(
    SelectionPointer *self,
    const char *key,
    void *call) {
  return static_cast<CuteSelectionPointer *>(self)->take(key, call);
}
