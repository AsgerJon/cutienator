//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(colordialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcolordialog.h"
#if QT_CONFIG(accessibility)
#include "qaccessible.h"
#endif
#include "qapplication.h"
#include "qdrawutil.h"
#include "qevent.h"
#include "qimage.h"
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include "qlabel.h"
#include "qlayout.h"
#include "qlineedit.h"
#if QT_CONFIG(menu)
#include "qmenu.h"
#endif
#include "qpainter.h"
#include "qpixmap.h"
#include "qpushbutton.h"
#if QT_CONFIG(regularexpression)
#include <qregularexpression.h>
#endif
#if QT_CONFIG(settings)
#include "qsettings.h"
#endif
#include "qsharedpointer.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qvalidator.h"
#include "qmimedata.h"
#include "qspinbox.h"
#include "qdialogbuttonbox.h"
#include "qscreen.h"
#include "qcursor.h"
#include "qtimer.h"
#include "qwindow.h"
#include "private/qdialog_p.h"
#include "private/qcolorwell_p.h"
#include <qpa/qplatformintegration.h>
#include <qpa/qplatformservices.h>
#include <private/qguiapplication_p.h>
#include <QtCore/qpointer.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/dialogs/qcolordialog.cpp, line 274, as _ZN10QWellArray15mousePressEventEP11QMouseEvent
inline void QWellArray::mousePressEvent(QMouseEvent *e)
{
    // The current cell marker is set to the cell the mouse is pressed in
    QPoint pos = e->position().toPoint();
    setCurrent(rowAt(pos.y()), columnAt(pos.x()));
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 281, as _ZN10QWellArray17mouseReleaseEventEP11QMouseEvent
inline void QWellArray::mouseReleaseEvent(QMouseEvent * /* event */)
{
    // The current cell marker is set to the cell the mouse is clicked in
    setSelected(curRow, curCol);
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 522, as _ZN10QColorWell17paintCellContentsEP8QPainteriiRK5QRect
inline void QColorWell::paintCellContents(QPainter *p, int row, int col, const QRect &r)
{
    int i = row + col*numRows();
    p->fillRect(r, QColor(values[i]));
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 528, as _ZN10QColorWell15mousePressEventEP11QMouseEvent
inline void QColorWell::mousePressEvent(QMouseEvent *e)
{
    oldCurrent = QPoint(selectedRow(), selectedColumn());
    QWellArray::mousePressEvent(e);
    mousePressed = true;
    pressPos = e->position().toPoint();
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 536, as _ZN10QColorWell14mouseMoveEventEP11QMouseEvent
inline void QColorWell::mouseMoveEvent(QMouseEvent *e)
{
    QWellArray::mouseMoveEvent(e);
#if QT_CONFIG(draganddrop)
    if (!mousePressed)
        return;
    if ((pressPos - e->position().toPoint()).manhattanLength() > QApplication::startDragDistance()) {
        setCurrent(oldCurrent.x(), oldCurrent.y());
        int i = rowAt(pressPos.y()) + columnAt(pressPos.x()) * numRows();
        QColor col(values[i]);
        QMimeData *mime = new QMimeData;
        mime->setColorData(col);
        QPixmap pix(cellWidth(), cellHeight());
        pix.fill(col);
        QPainter p(&pix);
        p.drawRect(0, 0, pix.width() - 1, pix.height() - 1);
        p.end();
        QDrag *drg = new QDrag(this);
        drg->setMimeData(mime);
        drg->setPixmap(pix);
        mousePressed = false;
        drg->exec(Qt::CopyAction);
    }
#endif
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 601, as _ZN10QColorWell17mouseReleaseEventEP11QMouseEvent
inline void QColorWell::mouseReleaseEvent(QMouseEvent *e)
{
    if (!mousePressed)
        return;
    QWellArray::mouseReleaseEvent(e);
    mousePressed = false;
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 563, as _ZN10QColorWell14dragEnterEventEP15QDragEnterEvent
#if QT_CONFIG(draganddrop)
inline void QColorWell::dragEnterEvent(QDragEnterEvent *e)
{
    if (qvariant_cast<QColor>(e->mimeData()->colorData()).isValid())
        e->accept();
    else
        e->ignore();
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/dialogs/qcolordialog.cpp, line 571, as _ZN10QColorWell14dragLeaveEventEP15QDragLeaveEvent
#if QT_CONFIG(draganddrop)
inline void QColorWell::dragLeaveEvent(QDragLeaveEvent *)
{
    if (hasFocus())
        parentWidget()->setFocus();
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/dialogs/qcolordialog.cpp, line 577, as _ZN10QColorWell13dragMoveEventEP14QDragMoveEvent
#if QT_CONFIG(draganddrop)
inline void QColorWell::dragMoveEvent(QDragMoveEvent *e)
{
    if (qvariant_cast<QColor>(e->mimeData()->colorData()).isValid()) {
        setCurrent(rowAt(e->position().toPoint().y()), columnAt(e->position().toPoint().x()));
        e->accept();
    } else {
        e->ignore();
    }
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/dialogs/qcolordialog.cpp, line 587, as _ZN10QColorWell9dropEventEP10QDropEvent
#if QT_CONFIG(draganddrop)
inline void QColorWell::dropEvent(QDropEvent *e)
{
    QColor col = qvariant_cast<QColor>(e->mimeData()->colorData());
    if (col.isValid()) {
        int i = rowAt(e->position().toPoint().y()) + columnAt(e->position().toPoint().x()) * numRows();
        emit colorChanged(i, col.rgb());
        e->accept();
    } else {
        e->ignore();
    }
}
#endif  // QT_CONFIG(draganddrop)
//  -----------------------------------------------------------------------

//  Only a class built on QColorWell may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQColorWell : QColorWell {
  using QColorWell::paintCellContents;
  using QColorWell::mousePressEvent;
  using QColorWell::mouseMoveEvent;
  using QColorWell::mouseReleaseEvent;
  using QColorWell::dragEnterEvent;
  using QColorWell::dragLeaveEvent;
  using QColorWell::dragMoveEvent;
};

//  const QMetaObject *QColorWell::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QColorWell10metaObjectEv(
    const QColorWell *self) {
  return self->metaObject();
}

//  void QColorWell::paintCellContents(QPainter *a0, int row, int col, const
//      QRect &a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell17paintCellContentsEP8QPainteriiRK5QRect(
    QColorWell *self,
    QPainter *a0,
    int row,
    int col,
    const QRect *a3) {
  self->paintCellContents(a0, row, col, *a3);
}

//  void QColorWell::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell15mousePressEventEP11QMouseEvent(
    QColorWell *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QColorWell::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell14mouseMoveEventEP11QMouseEvent(
    QColorWell *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QColorWell::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell17mouseReleaseEventEP11QMouseEvent(
    QColorWell *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

#if QT_CONFIG(draganddrop)
//  void QColorWell::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell14dragEnterEventEP15QDragEnterEvent(
    QColorWell *self,
    QDragEnterEvent *e) {
  self->dragEnterEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QColorWell::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell14dragLeaveEventEP15QDragLeaveEvent(
    QColorWell *self,
    QDragLeaveEvent *e) {
  self->dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QColorWell::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell13dragMoveEventEP14QDragMoveEvent(
    QColorWell *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QColorWell::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorWell9dropEventEP10QDropEvent(
    QColorWell *self,
    QDropEvent *e) {
  self->dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

//  void QColorWell::paintCellContents(QPainter *a0, int row, int col, const
//      QRect &a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell17paintCellContentsEP8QPainteriiRK5QRect(
    QColorWell *self,
    QPainter *a0,
    int row,
    int col,
    const QRect *a3) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::paintCellContents(
      a0,
      row,
      col,
      *a3);
}

//  void QColorWell::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell15mousePressEventEP11QMouseEvent(
    QColorWell *self,
    QMouseEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::mousePressEvent(e);
}

//  void QColorWell::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell14mouseMoveEventEP11QMouseEvent(
    QColorWell *self,
    QMouseEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::mouseMoveEvent(e);
}

//  void QColorWell::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell17mouseReleaseEventEP11QMouseEvent(
    QColorWell *self,
    QMouseEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::mouseReleaseEvent(e);
}

#if QT_CONFIG(draganddrop)
//  void QColorWell::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell14dragEnterEventEP15QDragEnterEvent(
    QColorWell *self,
    QDragEnterEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::dragEnterEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QColorWell::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell14dragLeaveEventEP15QDragLeaveEvent(
    QColorWell *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QColorWell::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell13dragMoveEventEP14QDragMoveEvent(
    QColorWell *self,
    QDragMoveEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#endif  // QT_CONFIG(colordialog)
