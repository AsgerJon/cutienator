//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#include "qitemeditorfactory.h"
#include "qitemeditorfactory_p.h"
#if QT_CONFIG(combobox)
#include <qcombobox.h>
#endif
#if QT_CONFIG(datetimeedit)
#include <qdatetimeedit.h>
#endif
#if QT_CONFIG(label)
#include <qlabel.h>
#endif
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#endif
#if QT_CONFIG(spinbox)
#include <qspinbox.h>
#endif
#include <qstyle.h>
#include <qstyleoption.h>
#include <limits.h>
#include <float.h>
#include <qapplication.h>
#include <qdebug.h>
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

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 546, as _ZN18QExpandingLineEdit16resizeToContentsEv
#if QT_CONFIG(lineedit)
inline void QExpandingLineEdit::resizeToContents()
{
    int oldWidth = width();
    if (originalWidth == -1)
        originalWidth = oldWidth;
    if (QWidget *parent = parentWidget()) {
        QPoint position = pos();
        int hintWidth = minimumWidth() + fontMetrics().horizontalAdvance(displayText());
        int parentWidth = parent->width();
        int maxWidth = isRightToLeft() ? position.x() + oldWidth : parentWidth - position.x();
        int newWidth = qBound(qMin(originalWidth, maxWidth), hintWidth, maxWidth);
        if (widgetOwnsGeometry)
            setMaximumWidth(newWidth);
        if (isRightToLeft())
            move(position.x() - newWidth + oldWidth, position.y());
        resize(newWidth, height());
    }
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

#if QT_CONFIG(lineedit)
//  void QExpandingLineEdit::resizeToContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit16resizeToContentsEv(
    QExpandingLineEdit *self) {
  self->resizeToContents();
}
#endif  // QT_CONFIG(lineedit)

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
