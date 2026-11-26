//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/drawer_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'Drawer' is pasted in, cut
//  from what the moc of Qt 6.12.0 writes for its header: Qt's library keeps
//  it to itself; added are 4 rituals that lean on what moc writes for a
//  class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/drawer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtOpenGL/QOpenGLShader>
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/q3dcamera_p.h>
#include <QtDataVisualization/private/q3dtheme_p.h>
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/qcustom3ditem_p.h>
#include <QtDataVisualization/private/qcustom3dlabel_p.h>
#include <QtDataVisualization/private/qcustom3dvolume_p.h>
#include <QtDataVisualization/private/scatter3drenderer_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QOffscreenSurface>
#include <QtCore/QThread>
#include <QtDataVisualization/private/labelitem_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 23, as local:drawer.cpp:point_data
//  Left out by hand: 'initResources' and 'Q_CONSTRUCTOR_FUNCTION(
//  initResources)' before this, which register the resources of
//  QtDataVisualization when the library opens: Qt's own library does
//  that, and the functions it calls Qt keeps to itself.
// Vertex array buffer for point
const GLfloat point_data[] = {0.0f, 0.0f, 0.0f};

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 31, as local:drawer.cpp:line_data
const GLfloat line_data[] = {
    -1.0f, 0.0f, 0.0f,
    1.0f, 0.0f, 0.0f,
};

//  from QtDataVisualization__Drawer.cpp, line 1, as moc:Drawer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN6DrawerE_t {};
} // unnamed namespace

template <> constexpr inline auto Drawer::qt_create_metaobjectdata<qt_meta_tag_ZN6DrawerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Drawer",
        "drawerChanged",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'drawerChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Drawer, qt_meta_tag_ZN6DrawerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Drawer::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN6DrawerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN6DrawerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN6DrawerE_t>.metaTypes,
    nullptr
} };

void Drawer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Drawer *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->drawerChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (Drawer::*)()>(_a, &Drawer::drawerChanged, 0))
            return;
    }
}

const QMetaObject *Drawer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Drawer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN6DrawerE_t>.strings))
        return static_cast<void*>(this);
    if (!strcmp(_clname, "QOpenGLFunctions"))
        return static_cast< QOpenGLFunctions*>(this);
    return QObject::qt_metacast(_clname);
}

int Drawer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void Drawer::drawerChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 37, as _ZN13TextureHelperD1Ev
inline TextureHelper::~TextureHelper()
{
#if !QT_CONFIG(opengles2)
    delete m_openGlFunctions_2_1;
#endif
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 377, as _ZN12ShaderHelper6posAttEv
inline GLint ShaderHelper::posAtt()
{
    if (!m_initialized)
        qFatal("Shader not initialized");
    return m_positionAttr;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 50, as _ZN20AbstractObjectHelper10elementBufEv
inline GLuint AbstractObjectHelper::elementBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_elementbuffer;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 57, as _ZN20AbstractObjectHelper10indexCountEv
inline GLuint AbstractObjectHelper::indexCount()
{
    return m_indexCount;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 29, as _ZN20AbstractObjectHelper9vertexBufEv
inline GLuint AbstractObjectHelper::vertexBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_vertexbuffer;
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

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 1115, as _ZN18Abstract3DRenderer14selectionLabelEv
inline QString &Abstract3DRenderer::selectionLabel()
{
    return m_selectionLabel;
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 1101, as _ZN18Abstract3DRenderer18selectionLabelItemEv
inline LabelItem &Abstract3DRenderer::selectionLabelItem()
{
    if (!m_selectionLabelItem)
        m_selectionLabelItem = new LabelItem;
    return *m_selectionLabelItem;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 29, as _ZN9LabelItem12setTextureIdEj
inline void LabelItem::setTextureId(GLuint textureId)
{
    QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = textureId;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 40, as _ZN9LabelItem5clearEv
inline void LabelItem::clear()
{
    if (m_textureId && QOpenGLContext::currentContext())
        QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = 0;
    m_size = QSize(0, 0);
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 19, as _ZN9LabelItem7setSizeERK5QSize
inline void LabelItem::setSize(const QSize &size)
{
    m_size = size;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 334, as _ZN13TextureHelper17convertToGLFormatERK6QImage
inline QImage TextureHelper::convertToGLFormat(const QImage &srcImage)
{
    QImage res(srcImage.size(), QImage::Format_ARGB32);
    convertToGLFormatHelper(res, srcImage.convertToFormat(QImage::Format_ARGB32), GL_RGBA);
    return res;
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 36, as _ZN6DrawerC1EP8Q3DTheme
inline Drawer::Drawer(Q3DTheme *theme)
    : m_theme(theme),
      m_textureHelper(0),
      m_pointbuffer(0),
      m_linebuffer(0),
      m_scaledFontSize(0.0f)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 45, as _ZN6DrawerD1Ev
inline Drawer::~Drawer()
{
    delete m_textureHelper;
    if (QOpenGLContext::currentContext()) {
        glDeleteBuffers(1, &m_pointbuffer);
        glDeleteBuffers(1, &m_linebuffer);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 61, as _ZN6Drawer8setThemeEP8Q3DTheme
inline void Drawer::setTheme(Q3DTheme *theme)
{
    m_theme = theme;
    m_scaledFontSize = 0.05f + m_theme->font().pointSizeF() / 500.0f;
    emit drawerChanged();
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 68, as _ZNK6Drawer5themeEv
inline Q3DTheme *Drawer::theme() const
{
    return m_theme;
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 73, as _ZNK6Drawer4fontEv
inline QFont Drawer::font() const
{
    return m_theme->font();
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 158, as _ZN6Drawer19drawSelectionObjectEP12ShaderHelperP20AbstractObjectHelper
inline void Drawer::drawSelectionObject(ShaderHelper *shader, AbstractObjectHelper *object)
{
    glEnableVertexAttribArray(shader->posAtt());
    glBindBuffer(GL_ARRAY_BUFFER, object->vertexBuf());
    glVertexAttribPointer(shader->posAtt(), 3, GL_FLOAT, GL_FALSE, 0, (void *)0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, object->elementBuf());
    glDrawElements(GL_TRIANGLES, object->indexCount(), GL_UNSIGNED_INT, (void *)0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glDisableVertexAttribArray(shader->posAtt());
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 194, as _ZN6Drawer9drawPointEP12ShaderHelper
inline void Drawer::drawPoint(ShaderHelper *shader)
{
    // Draw a single point

    // Generate vertex buffer for point if it does not exist
    if (!m_pointbuffer) {
        glGenBuffers(1, &m_pointbuffer);
        glBindBuffer(GL_ARRAY_BUFFER, m_pointbuffer);
        glBufferData(GL_ARRAY_BUFFER, sizeof(point_data), point_data, GL_STATIC_DRAW);
    }

    // 1st attribute buffer : vertices
    glEnableVertexAttribArray(shader->posAtt());
    glBindBuffer(GL_ARRAY_BUFFER, m_pointbuffer);
    glVertexAttribPointer(shader->posAtt(), 3, GL_FLOAT, GL_FALSE, 0, (void*)0);

    // Draw the point
    glDrawArrays(GL_POINTS, 0, 1);

    // Free buffers
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    glDisableVertexAttribArray(shader->posAtt());
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 255, as _ZN6Drawer8drawLineEP12ShaderHelper
inline void Drawer::drawLine(ShaderHelper *shader)
{
    // Draw a single line

    // Generate vertex buffer for line if it does not exist
    if (!m_linebuffer) {
        glGenBuffers(1, &m_linebuffer);
        glBindBuffer(GL_ARRAY_BUFFER, m_linebuffer);
        glBufferData(GL_ARRAY_BUFFER, sizeof(line_data), line_data, GL_STATIC_DRAW);
    }

    // 1st attribute buffer : vertices
    glEnableVertexAttribArray(shader->posAtt());
    glBindBuffer(GL_ARRAY_BUFFER, m_linebuffer);
    glVertexAttribPointer(shader->posAtt(), 3, GL_FLOAT, GL_FALSE, 0, (void*)0);

    // Draw the line
    glDrawArrays(GL_LINES, 0, 2);

    // Free buffers
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    glDisableVertexAttribArray(shader->posAtt());
}
//  -----------------------------------------------------------------------

//  A Drawer that Python can take functions over in. Every Drawer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDrawerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDrawerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDrawerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDrawerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDrawerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDrawerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDrawerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDrawer : public Drawer {
public:
  using Drawer::Drawer;
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
      CuteDrawerCall0 call = reinterpret_cast<CuteDrawerCall0>(taken[0]);
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
      CuteDrawerCall1 call = reinterpret_cast<CuteDrawerCall1>(taken[1]);
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
      CuteDrawerCall2 call = reinterpret_cast<CuteDrawerCall2>(taken[2]);
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
      CuteDrawerCall3 call = reinterpret_cast<CuteDrawerCall3>(taken[3]);
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
      CuteDrawerCall4 call = reinterpret_cast<CuteDrawerCall4>(taken[4]);
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
      CuteDrawerCall5 call = reinterpret_cast<CuteDrawerCall5>(taken[5]);
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
      CuteDrawerCall6 call = reinterpret_cast<CuteDrawerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Drawer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6Drawer10metaObjectEv(const Drawer *self) {
  return self->metaObject();
}

//  void *Drawer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN6Drawer11qt_metacastEPKc(Drawer *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int Drawer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN6Drawer11qt_metacallEN11QMetaObject4CallEiPPv(
    Drawer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Drawer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6Drawer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Drawer::tr(s, c, n));
}

//  Drawer::Drawer(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
Drawer *ritual_ZN6DrawerC1EP8Q3DTheme(Q3DTheme *theme) {
  return new CuteDrawer(theme);
}

//  Drawer::~Drawer()
extern "C" Q_DECL_EXPORT
void ritual_ZN6DrawerD1Ev(Drawer *self) {
  delete self;
}

//  void Drawer::setTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Drawer8setThemeEP8Q3DTheme(Drawer *self, Q3DTheme *theme) {
  self->setTheme(theme);
}

//  Q3DTheme *Drawer::theme() const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZNK6Drawer5themeEv(const Drawer *self) {
  return self->theme();
}

//  QFont Drawer::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK6Drawer4fontEv(const Drawer *self) {
  return new QFont(self->font());
}

//  GLfloat Drawer::scaledFontSize() const
extern "C" Q_DECL_EXPORT
GLfloat ritual_ZNK6Drawer14scaledFontSizeEv(const Drawer *self) {
  return self->scaledFontSize();
}

//  void Drawer::drawSelectionObject(ShaderHelper *shader,
//      AbstractObjectHelper *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Drawer19drawSelectionObjectEP12ShaderHelperP20AbstractObjectHelper(
    Drawer *self,
    ShaderHelper *shader,
    AbstractObjectHelper *object) {
  self->drawSelectionObject(shader, object);
}

//  void Drawer::drawPoint(ShaderHelper *shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Drawer9drawPointEP12ShaderHelper(
    Drawer *self,
    ShaderHelper *shader) {
  self->drawPoint(shader);
}

//  void Drawer::drawLine(ShaderHelper *shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Drawer8drawLineEP12ShaderHelper(
    Drawer *self,
    ShaderHelper *shader) {
  self->drawLine(shader);
}

//  void Drawer::drawerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN6Drawer13drawerChangedEv(Drawer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Drawer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "drawerChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "drawerChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  Drawer as the QOpenGLFunctions it is built on
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_cast_Drawer_QOpenGLFunctions(Drawer *self) {
  return static_cast<QOpenGLFunctions *>(self);
}

//  a Python function taken by a CuteDrawer, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Drawer(Drawer *self, const char *key, void *call) {
  return static_cast<CuteDrawer *>(self)->take(key, call);
}
