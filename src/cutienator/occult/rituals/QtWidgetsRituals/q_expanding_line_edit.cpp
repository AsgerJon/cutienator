//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#include <QtWidgets/qitemeditorfactory.h>
#include <QtWidgets/private/qitemeditorfactory_p.h>
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(datetimeedit)
#include <QtWidgets/qdatetimeedit.h>
#endif
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(spinbox)
#include <QtWidgets/qspinbox.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <limits.h>
#include <float.h>
#include <QtWidgets/qapplication.h>
#include <QtCore/qdebug.h>
#include <vector>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 517, as _ZN18QExpandingLineEdit11changeEventEP6QEvent
#if QT_CONFIG(lineedit)
inline void QExpandingLineEdit::changeEvent(QEvent *e)
{
    switch (e->type())
    {
    case QEvent::FontChange:
    case QEvent::StyleChange:
    case QEvent::ContentsRectChange:
        updateMinimumWidth();
        break;
    default:
        break;
    }

    QLineEdit::changeEvent(e);
}
#endif  // QT_CONFIG(lineedit)

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 533, as _ZN18QExpandingLineEdit18updateMinimumWidthEv
#if QT_CONFIG(lineedit)
inline void QExpandingLineEdit::updateMinimumWidth()
{
    const QMargins tm = textMargins();
    const QMargins cm = contentsMargins();
    const int width = tm.left() + tm.right() + cm.left() + cm.right() + 4 /*horizontalMargin in qlineedit.cpp*/;

    QStyleOptionFrame opt;
    initStyleOption(&opt);

    int minWidth = style()->sizeFromContents(QStyle::CT_LineEdit, &opt, QSize(width, 0), this).width();
    setMinimumWidth(minWidth);
}
#endif  // QT_CONFIG(lineedit)
//  -----------------------------------------------------------------------

//  Only a class built on QExpandingLineEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQExpandingLineEdit : QExpandingLineEdit {
  using QExpandingLineEdit::changeEvent;
};

//  const QMetaObject *QExpandingLineEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QExpandingLineEdit10metaObjectEv(
    const QExpandingLineEdit *self) {
  return self->metaObject();
}

//  void *QExpandingLineEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QExpandingLineEdit11qt_metacastEPKc(
    QExpandingLineEdit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QExpandingLineEdit::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QExpandingLineEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    QExpandingLineEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QExpandingLineEdit::setWidgetOwnsGeometry(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit21setWidgetOwnsGeometryEb(
    QExpandingLineEdit *self,
    bool value) {
  self->setWidgetOwnsGeometry(value);
}

//  void QExpandingLineEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit11changeEventEP6QEvent(
    QExpandingLineEdit *self,
    QEvent *e) {
  self->changeEvent(e);
}

//  void QExpandingLineEdit::resizeToContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit16resizeToContentsEv(
    QExpandingLineEdit *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QExpandingLineEdit")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resizeToContents()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resizeToContents()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(lineedit)
//  void QExpandingLineEdit::updateMinimumWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit18updateMinimumWidthEv(
    QExpandingLineEdit *self) {
  self->updateMinimumWidth();
}
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
//  void QExpandingLineEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QExpandingLineEdit11changeEventEP6QEvent(
    QExpandingLineEdit *self,
    QEvent *e) {
  static_cast<OwnQExpandingLineEdit *>(self)->OwnQExpandingLineEdit::changeEvent(
      e);
}
#endif  // QT_CONFIG(lineedit)

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
