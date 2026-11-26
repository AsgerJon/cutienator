//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3ditem_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QCustom3DItemPrivate' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3ditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qcustom3ditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__QCustom3DItemPrivate.cpp, line 1, as moc:QCustom3DItemPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QCustom3DItemPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QCustom3DItemPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN20QCustom3DItemPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QCustom3DItemPrivate",
        "needUpdate",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'needUpdate'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QCustom3DItemPrivate, qt_meta_tag_ZN20QCustom3DItemPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QCustom3DItemPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QCustom3DItemPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QCustom3DItemPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QCustom3DItemPrivateE_t>.metaTypes,
    nullptr
} };

void QCustom3DItemPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QCustom3DItemPrivate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->needUpdate(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QCustom3DItemPrivate::*)()>(_a, &QCustom3DItemPrivate::needUpdate, 0))
            return;
    }
}

const QMetaObject *QCustom3DItemPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QCustom3DItemPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QCustom3DItemPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QCustom3DItemPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
void QCustom3DItemPrivate::needUpdate()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 493, as _ZN20QCustom3DItemPrivateD0Ev
inline QCustom3DItemPrivate::~QCustom3DItemPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 460, as _ZN20QCustom3DItemPrivateC1EP13QCustom3DItem
inline QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q) :
    q_ptr(q),
    m_textureImage(QImage(1, 1, QImage::Format_ARGB32)),
    m_position(QVector3D(0.0f, 0.0f, 0.0f)),
    m_positionAbsolute(false),
    m_scaling(QVector3D(0.1f, 0.1f, 0.1f)),
    m_scalingAbsolute(true),
    m_rotation(identityQuaternion),
    m_visible(true),
    m_shadowCasting(true),
    m_isLabelItem(false),
    m_isVolumeItem(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 475, as _ZN20QCustom3DItemPrivateC1EP13QCustom3DItemRK7QStringRK9QVector3DS7_RK11QQuaternion
inline QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q, const QString &meshFile,
                                           const QVector3D &position, const QVector3D &scaling,
                                           const QQuaternion &rotation) :
    q_ptr(q),
    m_textureImage(QImage(1, 1, QImage::Format_ARGB32)),
    m_meshFile(meshFile),
    m_position(position),
    m_positionAbsolute(false),
    m_scaling(scaling),
    m_scalingAbsolute(true),
    m_rotation(rotation),
    m_visible(true),
    m_shadowCasting(true),
    m_isLabelItem(false),
    m_isVolumeItem(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 497, as _ZN20QCustom3DItemPrivate12textureImageEv
inline QImage QCustom3DItemPrivate::textureImage()
{
    return m_textureImage;
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 502, as _ZN20QCustom3DItemPrivate17clearTextureImageEv
inline void QCustom3DItemPrivate::clearTextureImage()
{
    m_textureImage = QImage();
    m_textureFile.clear();
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 508, as _ZN20QCustom3DItemPrivate14resetDirtyBitsEv
inline void QCustom3DItemPrivate::resetDirtyBits()
{
    m_dirtyBits.textureDirty = false;
    m_dirtyBits.meshDirty = false;
    m_dirtyBits.positionDirty = false;
    m_dirtyBits.scalingDirty = false;
    m_dirtyBits.rotationDirty = false;
    m_dirtyBits.visibleDirty = false;
    m_dirtyBits.shadowCastingDirty = false;
}
//  -----------------------------------------------------------------------

//  A QCustom3DItemPrivate that Python can take functions over in. Every QCustom3DItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DItemPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DItemPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustom3DItemPrivate : public QCustom3DItemPrivate {
public:
  using QCustom3DItemPrivate::QCustom3DItemPrivate;
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
      CuteQCustom3DItemPrivateCall0 call = reinterpret_cast<CuteQCustom3DItemPrivateCall0>(taken[0]);
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
      CuteQCustom3DItemPrivateCall1 call = reinterpret_cast<CuteQCustom3DItemPrivateCall1>(taken[1]);
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
      CuteQCustom3DItemPrivateCall2 call = reinterpret_cast<CuteQCustom3DItemPrivateCall2>(taken[2]);
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
      CuteQCustom3DItemPrivateCall3 call = reinterpret_cast<CuteQCustom3DItemPrivateCall3>(taken[3]);
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
      CuteQCustom3DItemPrivateCall4 call = reinterpret_cast<CuteQCustom3DItemPrivateCall4>(taken[4]);
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
      CuteQCustom3DItemPrivateCall5 call = reinterpret_cast<CuteQCustom3DItemPrivateCall5>(taken[5]);
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
      CuteQCustom3DItemPrivateCall6 call = reinterpret_cast<CuteQCustom3DItemPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustom3DItemPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QCustom3DItemPrivate10metaObjectEv(
    const QCustom3DItemPrivate *self) {
  return self->metaObject();
}

//  void *QCustom3DItemPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QCustom3DItemPrivate11qt_metacastEPKc(
    QCustom3DItemPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCustom3DItemPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QCustom3DItemPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QCustom3DItemPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCustom3DItemPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QCustom3DItemPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCustom3DItemPrivate::tr(s, c, n));
}

//  QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q)
extern "C" Q_DECL_EXPORT
QCustom3DItemPrivate *ritual_ZN20QCustom3DItemPrivateC1EP13QCustom3DItem(
    QCustom3DItem *q) {
  return new CuteQCustom3DItemPrivate(q);
}

//  QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q, const
//      QString &meshFile, const QVector3D &position, const QVector3D
//      &scaling, const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
QCustom3DItemPrivate *ritual_ZN20QCustom3DItemPrivateC1EP13QCustom3DItemRK7QStringRK9QVector3DS7_RK11QQuaternion(
    QCustom3DItem *q,
    const QString *meshFile,
    const QVector3D *position,
    const QVector3D *scaling,
    const QQuaternion *rotation) {
  return new CuteQCustom3DItemPrivate(
      q,
      *meshFile,
      *position,
      *scaling,
      *rotation);
}

//  QCustom3DItemPrivate::~QCustom3DItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivateD1Ev(QCustom3DItemPrivate *self) {
  delete self;
}

//  QImage QCustom3DItemPrivate::textureImage()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN20QCustom3DItemPrivate12textureImageEv(
    QCustom3DItemPrivate *self) {
  return new QImage(self->textureImage());
}

//  void QCustom3DItemPrivate::clearTextureImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivate17clearTextureImageEv(
    QCustom3DItemPrivate *self) {
  self->clearTextureImage();
}

//  void QCustom3DItemPrivate::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivate14resetDirtyBitsEv(
    QCustom3DItemPrivate *self) {
  self->resetDirtyBits();
}

//  void QCustom3DItemPrivate::needUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivate10needUpdateEv(
    QCustom3DItemPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCustom3DItemPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "needUpdate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "needUpdate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQCustom3DItemPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustom3DItemPrivate(
    QCustom3DItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustom3DItemPrivate *>(self)->take(key, call);
}
