//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#include <QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 15, as local:qquick3dxractionmapper.cpp:actionIntKey
static inline quint32 actionIntKey(const QQuick3DXrInputAction::Action id, const QtQuick3DXr::Controller controller)
{
    return quint16(id) | (quint32(controller) << 16);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 20, as local:qquick3dxractionmapper.cpp:actionStringKey
static inline QString actionStringKey(const QString &name, const QtQuick3DXr::Controller controller)
{
    return QString::number(uint(controller)) + name;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 221, as _ZN21QQuick3DXrInputAction10classBeginEv
inline void QQuick3DXrInputAction::classBegin()
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 225, as _ZN21QQuick3DXrInputAction17componentCompleteEv
inline void QQuick3DXrInputAction::componentComplete()
{
    QQuick3DXrActionMapper::registerAction(this);
    m_componentComplete = true;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 62, as _ZN22QQuick3DXrActionMapper14registerActionEP21QQuick3DXrInputAction
inline void QQuick3DXrActionMapper::registerAction(QQuick3DXrInputAction *action)
{
    auto *that = instance();

    const auto &idList = action->actionId();
    const auto controller = static_cast<QtQuick3DXr::Controller>(action->controller());

    if (idList.isEmpty()) {
        that->m_customActions.insert(actionStringKey(action->actionName(), controller), action);
    } else {
        for (const auto &id : idList) {
            if (id != QQuick3DXrInputAction::CustomAction)
                that->m_actions.insert(actionIntKey(id, controller), action);
        }
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 25, as _ZN22QQuick3DXrActionMapper8instanceEv
inline QQuick3DXrActionMapper *QQuick3DXrActionMapper::instance()
{
    static QQuick3DXrActionMapper instance;
    return &instance;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 11, as _ZN22QQuick3DXrActionMapperC1EP7QObject
inline QQuick3DXrActionMapper::QQuick3DXrActionMapper(QObject *parent) : QObject(parent)
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 216, as _ZNK21QQuick3DXrInputAction5valueEv
inline float QQuick3DXrInputAction::value() const
{
    return m_value;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 158, as _ZNK21QQuick3DXrInputAction7pressedEv
inline bool QQuick3DXrInputAction::pressed() const
{
    return m_pressed;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 180, as _ZNK21QQuick3DXrInputAction10actionNameEv
inline QString QQuick3DXrInputAction::actionName() const
{
    return m_actionName;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 268, as _ZNK21QQuick3DXrInputAction8actionIdEv
inline QList<QQuick3DXrInputAction::Action> QQuick3DXrInputAction::actionId() const
{
    return m_actionIds;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 303, as _ZNK21QQuick3DXrInputAction4handEv
inline QQuick3DXrInputAction::Controller QQuick3DXrInputAction::hand() const
{
    return static_cast<Controller>(m_controller);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 353, as _ZNK21QQuick3DXrInputAction7enabledEv
inline bool QQuick3DXrInputAction::enabled() const
{
    return m_enabled;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 331, as _ZNK21QQuick3DXrInputAction10controllerEv
inline QQuick3DXrInputAction::Controller QQuick3DXrInputAction::controller() const
{
    return static_cast<Controller>(m_controller);
}
//  -----------------------------------------------------------------------

//  A QQuick3DXrInputAction that Python can take functions over in. Every QQuick3DXrInputAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DXrInputActionCall0)(const void *, int *);
typedef void (*CuteQQuick3DXrInputActionCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrInputActionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrInputActionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrInputActionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrInputActionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrInputActionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrInputActionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrInputActionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrInputAction : public QQuick3DXrInputAction {
public:
  using QQuick3DXrInputAction::QQuick3DXrInputAction;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DXrInputAction::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall0 call = reinterpret_cast<CuteQQuick3DXrInputActionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DXrInputAction::classBegin();
  }

  //  void QQuick3DXrInputAction::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall1 call = reinterpret_cast<CuteQQuick3DXrInputActionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DXrInputAction::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall2 call = reinterpret_cast<CuteQQuick3DXrInputActionCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall3 call = reinterpret_cast<CuteQQuick3DXrInputActionCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall4 call = reinterpret_cast<CuteQQuick3DXrInputActionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall5 call = reinterpret_cast<CuteQQuick3DXrInputActionCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall6 call = reinterpret_cast<CuteQQuick3DXrInputActionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall7 call = reinterpret_cast<CuteQQuick3DXrInputActionCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DXrInputActionCall8 call = reinterpret_cast<CuteQQuick3DXrInputActionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrInputAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DXrInputAction10metaObjectEv(
    const QQuick3DXrInputAction *self) {
  return self->metaObject();
}

//  void *QQuick3DXrInputAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuick3DXrInputAction11qt_metacastEPKc(
    QQuick3DXrInputAction *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrInputAction::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuick3DXrInputAction11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrInputAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DXrInputAction::~QQuick3DXrInputAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputActionD1Ev(QQuick3DXrInputAction *self) {
  delete self;
}

//  float QQuick3DXrInputAction::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DXrInputAction5valueEv(
    const QQuick3DXrInputAction *self) {
  return self->value();
}

//  bool QQuick3DXrInputAction::pressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DXrInputAction7pressedEv(
    const QQuick3DXrInputAction *self) {
  return self->pressed();
}

//  QString QQuick3DXrInputAction::actionName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DXrInputAction10actionNameEv(
    const QQuick3DXrInputAction *self) {
  return new QString(self->actionName());
}

//  QList<Action> QQuick3DXrInputAction::actionId() const
extern "C" Q_DECL_EXPORT
QList<QQuick3DXrInputAction::Action> *ritual_ZNK21QQuick3DXrInputAction8actionIdEv(
    const QQuick3DXrInputAction *self) {
  return new QList<QQuick3DXrInputAction::Action>(self->actionId());
}

//  void QQuick3DXrInputAction::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction10classBeginEv(
    QQuick3DXrInputAction *self) {
  self->classBegin();
}

//  void QQuick3DXrInputAction::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction17componentCompleteEv(
    QQuick3DXrInputAction *self) {
  self->componentComplete();
}

//  Controller QQuick3DXrInputAction::hand() const
extern "C" Q_DECL_EXPORT
QQuick3DXrInputAction::Controller ritual_ZNK21QQuick3DXrInputAction4handEv(
    const QQuick3DXrInputAction *self) {
  return self->hand();
}

//  bool QQuick3DXrInputAction::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DXrInputAction7enabledEv(
    const QQuick3DXrInputAction *self) {
  return self->enabled();
}

//  Controller QQuick3DXrInputAction::controller() const
extern "C" Q_DECL_EXPORT
QQuick3DXrInputAction::Controller ritual_ZNK21QQuick3DXrInputAction10controllerEv(
    const QQuick3DXrInputAction *self) {
  return self->controller();
}

//  void QQuick3DXrInputAction::valueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction12valueChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "valueChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "valueChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::pressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction14pressedChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pressedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pressedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::triggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction9triggeredEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "triggered()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "triggered()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::actionNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction17actionNameChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "actionNameChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "actionNameChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::actionIdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction15actionIdChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "actionIdChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "actionIdChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::handChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction11handChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction14enabledChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrInputAction::controllerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrInputAction17controllerChangedEv(
    QQuick3DXrInputAction *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrInputAction")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controllerChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controllerChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuick3DXrInputAction as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DXrInputAction_QQmlParserStatus(
    QQuick3DXrInputAction *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DXrInputAction, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrInputAction(
    QQuick3DXrInputAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrInputAction *>(self)->take(key, call);
}

//  void QQuick3DXrInputAction::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuick3DXrInputAction10classBeginEv(
    QQuick3DXrInputAction *self) {
  self->QQuick3DXrInputAction::classBegin();
}

//  a QList<QQuick3DXrInputAction::Action> a ritual of QQuick3DXrInputAction
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DXrInputAction__QList_QQuick3DXrInputAction_Action(
    QList<QQuick3DXrInputAction::Action> *self) {
  delete self;
}
