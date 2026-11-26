//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QSGBatchRenderer::ShaderManager' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qsgbatchrenderer_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QElapsedTimer>
#include <QtCore/QtNumeric>
#include <QtGui/QGuiApplication>
#include <QtCore/private/qnumeric_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtQuick/private/qsgrhivisualizer_p.h>
#include <QtQuick/private/qsgnode_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 50, as local:qsgbatchrenderer.cpp:size_of_type
namespace QSGBatchRenderer {
static inline int size_of_type(int type)
{
    static int sizes[] = {
        sizeof(char),
        sizeof(unsigned char),
        sizeof(short),
        sizeof(unsigned short),
        sizeof(int),
        sizeof(unsigned int),
        sizeof(float),
        2,
        3,
        4,
        sizeof(double)
    };
    Q_ASSERT(type >= QSGGeometry::ByteType && type <= QSGGeometry::DoubleType);
    return sizes[type - QSGGeometry::ByteType];
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 83, as local:qsgbatchrenderer.cpp:VERTEX_BUFFER_BINDING
namespace QSGBatchRenderer {
const int VERTEX_BUFFER_BINDING = 0;
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 84, as local:qsgbatchrenderer.cpp:ZORDER_BUFFER_BINDING
namespace QSGBatchRenderer {
const int ZORDER_BUFFER_BINDING = VERTEX_BUFFER_BINDING + 1;
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 219, as local:qsgbatchrenderer.cpp:qsg_setMultiViewFlagsOnMaterial
namespace QSGBatchRenderer {
inline void qsg_setMultiViewFlagsOnMaterial(QSGMaterial *material, int multiViewCount)
{
    material->setFlag(QSGMaterial::MultiView2, multiViewCount == 2);
    material->setFlag(QSGMaterial::MultiView3, multiViewCount == 3);
    material->setFlag(QSGMaterial::MultiView4, multiViewCount == 4);
}
}  // namespace QSGBatchRenderer

//  from QtQuick__QSGBatchRenderer_ShaderManager.cpp, line 1, as moc:QSGBatchRenderer::ShaderManager
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t {};
} // unnamed namespace

template <> constexpr inline auto QSGBatchRenderer::ShaderManager::qt_create_metaobjectdata<qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSGBatchRenderer::ShaderManager",
        "invalidated",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'invalidated'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<ShaderManager, qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSGBatchRenderer::ShaderManager::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t>.metaTypes,
    nullptr
} };

void QSGBatchRenderer::ShaderManager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<ShaderManager *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->invalidated(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QSGBatchRenderer::ShaderManager::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSGBatchRenderer::ShaderManager::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QSGBatchRenderer13ShaderManagerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QSGBatchRenderer::ShaderManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 287, as _ZN16QSGBatchRenderer13ShaderManager11invalidatedEv
namespace QSGBatchRenderer {
inline void ShaderManager::invalidated()
{
    qDeleteAll(stockShaders);
    stockShaders.clear();
    qDeleteAll(rewrittenShaders);
    rewrittenShaders.clear();

    qDeleteAll(pipelineCache);
    pipelineCache.clear();

    qDeleteAll(srbPool);
    srbPool.clear();
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 301, as _ZN16QSGBatchRenderer13ShaderManager23clearCachedRendererDataEv
namespace QSGBatchRenderer {
inline void ShaderManager::clearCachedRendererData()
{
    for (ShaderManager::Shader *sms : std::as_const(stockShaders)) {
        QSGMaterialShader *s = sms->materialShader;
        if (s) {
            QSGMaterialShaderPrivate *sd = QSGMaterialShaderPrivate::get(s);
            sd->clearCachedRendererData();
        }
    }
    for (ShaderManager::Shader *sms : std::as_const(rewrittenShaders)) {
        QSGMaterialShader *s = sms->materialShader;
        if (s) {
            QSGMaterialShaderPrivate *sd = QSGMaterialShaderPrivate::get(s);
            sd->clearCachedRendererData();
        }
    }
}
}  // namespace QSGBatchRenderer
//  -----------------------------------------------------------------------

//  A QSGBatchRenderer::ShaderManager that Python can take functions over in. Every QSGBatchRenderer::ShaderManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGBatchRenderer_ShaderManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGBatchRenderer_ShaderManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_ShaderManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_ShaderManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_ShaderManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_ShaderManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_ShaderManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGBatchRenderer_ShaderManager : public QSGBatchRenderer::ShaderManager {
public:
  using QSGBatchRenderer::ShaderManager::ShaderManager;
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
      CuteQSGBatchRenderer_ShaderManagerCall0 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall0>(taken[0]);
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
      CuteQSGBatchRenderer_ShaderManagerCall1 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall1>(taken[1]);
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
      CuteQSGBatchRenderer_ShaderManagerCall2 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall2>(taken[2]);
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
      CuteQSGBatchRenderer_ShaderManagerCall3 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall3>(taken[3]);
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
      CuteQSGBatchRenderer_ShaderManagerCall4 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall4>(taken[4]);
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
      CuteQSGBatchRenderer_ShaderManagerCall5 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall5>(taken[5]);
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
      CuteQSGBatchRenderer_ShaderManagerCall6 call = reinterpret_cast<CuteQSGBatchRenderer_ShaderManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGBatchRenderer::ShaderManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSGBatchRenderer13ShaderManager10metaObjectEv(
    const QSGBatchRenderer::ShaderManager *self) {
  return self->metaObject();
}

//  void *QSGBatchRenderer::ShaderManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSGBatchRenderer13ShaderManager11qt_metacastEPKc(
    QSGBatchRenderer::ShaderManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGBatchRenderer::ShaderManager::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSGBatchRenderer13ShaderManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGBatchRenderer::ShaderManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGBatchRenderer::ShaderManager::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSGBatchRenderer13ShaderManager2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGBatchRenderer::ShaderManager::tr(s, c, n));
}

//  QSGBatchRenderer::ShaderManager::ShaderManager(QSGDefaultRenderContext
//      *ctx)
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::ShaderManager *ritual_ZN16QSGBatchRenderer13ShaderManagerC1EP23QSGDefaultRenderContext(
    QSGDefaultRenderContext *ctx) {
  return new CuteQSGBatchRenderer_ShaderManager(ctx);
}

//  QSGBatchRenderer::ShaderManager::~ShaderManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13ShaderManagerD1Ev(
    QSGBatchRenderer::ShaderManager *self) {
  delete self;
}

//  void QSGBatchRenderer::ShaderManager::clearCachedRendererData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13ShaderManager23clearCachedRendererDataEv(
    QSGBatchRenderer::ShaderManager *self) {
  self->clearCachedRendererData();
}

//  void QSGBatchRenderer::ShaderManager::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13ShaderManager11invalidatedEv(
    QSGBatchRenderer::ShaderManager *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSGBatchRenderer::ShaderManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "invalidated()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "invalidated()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQSGBatchRenderer_ShaderManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBatchRenderer_ShaderManager(
    QSGBatchRenderer::ShaderManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBatchRenderer_ShaderManager *>(self)->take(key, call);
}
