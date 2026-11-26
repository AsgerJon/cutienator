//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgrhiatlastexture_p.h>
#include <QtCore/QVarLengthArray>
#include <QtCore/QElapsedTimer>
#include <QtCore/QtMath>
#include <QtGui/QWindow>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgcompressedtexture_p.h>
#include <QtQuick/private/qsgcompressedatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 189, as _ZN18QSGRhiAtlasTexture5Atlas6createERK6QImage
namespace QSGRhiAtlasTexture {
inline Texture *Atlas::create(const QImage &image)
{
    // No need to lock, as manager already locked it.
    QRect rect = m_allocator.allocate(QSize(image.width() + 2, image.height() + 2));
    if (rect.width() > 0 && rect.height() > 0) {
        Texture *t = new Texture(this, rect, image);
        m_pending_uploads << t;
        return t;
    }
    return nullptr;
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 131, as _ZN18QSGRhiAtlasTexture9AtlasBase10invalidateEv
namespace QSGRhiAtlasTexture {
inline void AtlasBase::invalidate()
{
    delete m_texture;
    m_texture = nullptr;
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 57, as _ZN18QSGRhiAtlasTexture7ManagerD1Ev
namespace QSGRhiAtlasTexture {
inline Manager::~Manager()
{
    Q_ASSERT(m_atlas == nullptr);
    Q_ASSERT(m_atlases.isEmpty());
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 63, as _ZN18QSGRhiAtlasTexture7Manager10invalidateEv
namespace QSGRhiAtlasTexture {
inline void Manager::invalidate()
{
    if (m_atlas) {
        m_atlas->invalidate();
        m_atlas->deleteLater();
        m_atlas = nullptr;
    }

    QHash<unsigned int, QSGCompressedAtlasTexture::Atlas*>::iterator i = m_atlases.begin();
    while (i != m_atlases.end()) {
        i.value()->invalidate();
        i.value()->deleteLater();
        ++i;
    }
    m_atlases.clear();
}
}  // namespace QSGRhiAtlasTexture
//  -----------------------------------------------------------------------

//  A QSGRhiAtlasTexture::Manager that Python can take functions over in. Every QSGRhiAtlasTexture::Manager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_ManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_ManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_ManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_ManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_ManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_ManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_ManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_Manager : public QSGRhiAtlasTexture::Manager {
public:
  using QSGRhiAtlasTexture::Manager::Manager;
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
      CuteQSGRhiAtlasTexture_ManagerCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall0>(taken[0]);
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
      CuteQSGRhiAtlasTexture_ManagerCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall1>(taken[1]);
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
      CuteQSGRhiAtlasTexture_ManagerCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall2>(taken[2]);
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
      CuteQSGRhiAtlasTexture_ManagerCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall3>(taken[3]);
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
      CuteQSGRhiAtlasTexture_ManagerCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall4>(taken[4]);
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
      CuteQSGRhiAtlasTexture_ManagerCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall5>(taken[5]);
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
      CuteQSGRhiAtlasTexture_ManagerCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_ManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiAtlasTexture::Manager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGRhiAtlasTexture7Manager10metaObjectEv(
    const QSGRhiAtlasTexture::Manager *self) {
  return self->metaObject();
}

//  void *QSGRhiAtlasTexture::Manager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QSGRhiAtlasTexture7Manager11qt_metacastEPKc(
    QSGRhiAtlasTexture::Manager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRhiAtlasTexture::Manager::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QSGRhiAtlasTexture7Manager11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRhiAtlasTexture::Manager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSGRhiAtlasTexture::Manager::~Manager()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7ManagerD1Ev(
    QSGRhiAtlasTexture::Manager *self) {
  delete self;
}

//  void QSGRhiAtlasTexture::Manager::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7Manager10invalidateEv(
    QSGRhiAtlasTexture::Manager *self) {
  self->invalidate();
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_Manager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_Manager(
    QSGRhiAtlasTexture::Manager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_Manager *>(self)->take(key, call);
}
