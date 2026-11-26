//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolstate_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQStyleKitControlState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQStyleKitControlState10metaObjectEv(
    const QQStyleKitControlState *self) {
  return self->metaObject();
}

//  void *QQStyleKitControlState::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQStyleKitControlState11qt_metacastEPKc(
    QQStyleKitControlState *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitControlState::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQStyleKitControlState11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitControlState *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQSK::State QQStyleKitControlState::nestedState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQStyleKitControlState11nestedStateEv(
    const QQStyleKitControlState *self) {
  return static_cast<int>(self->nestedState().toInt());
}

//  void QQStyleKitControlState::pressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState14pressedChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
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

//  void QQStyleKitControlState::hoveredChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState14hoveredChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "hoveredChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "hoveredChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControlState::focusedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState14focusedChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "focusedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "focusedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControlState::checkedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState14checkedChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControlState::disabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState15disabledChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "disabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "disabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControlState::highlightedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState18highlightedChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "highlightedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "highlightedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControlState::verticalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQStyleKitControlState15verticalChangedEv(
    QQStyleKitControlState *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControlState")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "verticalChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "verticalChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
