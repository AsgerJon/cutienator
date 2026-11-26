//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 43, as _ZNK17QQStyleKitPalette15fallbackPaletteEv
inline QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
{
    return m_fallbackPalette;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitPalette::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQStyleKitPalette10metaObjectEv(
    const QQStyleKitPalette *self) {
  return self->metaObject();
}

//  void *QQStyleKitPalette::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQStyleKitPalette11qt_metacastEPKc(
    QQStyleKitPalette *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitPalette::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQStyleKitPalette11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitPalette *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
extern "C" Q_DECL_EXPORT
QQStyleKitPalette *ritual_ZNK17QQStyleKitPalette15fallbackPaletteEv(
    const QQStyleKitPalette *self) {
  return self->fallbackPalette();
}

//  void QQStyleKitPalette::systemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette13systemChangedEv(QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "systemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "systemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::checkBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette15checkBoxChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::buttonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette13buttonChangedEv(QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "buttonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "buttonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::comboBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette15comboBoxChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "comboBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "comboBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::groupBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette15groupBoxChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "groupBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "groupBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::itemDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette19itemDelegateChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemDelegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemDelegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::labelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette12labelChangedEv(QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "labelChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "labelChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::radioButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette18radioButtonChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "radioButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "radioButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::spinBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette14spinBoxChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "spinBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "spinBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::switchControlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette20switchControlChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "switchControlChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "switchControlChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::tabBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette13tabBarChangedEv(QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tabBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tabBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::textAreaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette15textAreaChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textAreaChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textAreaChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::textFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette16textFieldChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textFieldChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textFieldChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::toolBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette14toolBarChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "toolBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "toolBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitPalette::fallbackPaletteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette22fallbackPaletteChangedEv(
    QQStyleKitPalette *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitPalette")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fallbackPaletteChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fallbackPaletteChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QQStyleKitPalette::isSet(QQuickTheme::Scope scope) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQStyleKitPalette5isSetEN11QQuickTheme5ScopeE(
    const QQStyleKitPalette *self,
    QQuickTheme::Scope scope) {
  return self->isSet(scope);
}

//  void QQStyleKitPalette::markSet(QQuickTheme::Scope scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette7markSetEN11QQuickTheme5ScopeE(
    QQStyleKitPalette *self,
    QQuickTheme::Scope scope) {
  self->markSet(scope);
}
