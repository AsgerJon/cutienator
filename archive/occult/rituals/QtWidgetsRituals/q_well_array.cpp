//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
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

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/dialogs/qcolordialog.cpp, line 293, as _ZN10QWellArray10setCurrentEii
inline void QWellArray::setCurrent(int row, int col)
{
    if ((curRow == row) && (curCol == col))
        return;

    if (row < 0 || col < 0 || row >= nrows || col >= ncols)
        row = col = -1;

    int oldRow = curRow;
    int oldCol = curCol;

    curRow = row;
    curCol = col;

    updateCell(oldRow, oldCol);
    updateCell(curRow, curCol);

    emit currentChanged(curRow, curCol);
    sendAccessibleChildFocusEvent();
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 320, as _ZN10QWellArray11setSelectedEii
inline void QWellArray::setSelected(int row, int col)
{
    int oldRow = selRow;
    int oldCol = selCol;

    if (row < 0 || col < 0)
        row = col = -1;

    selCol = col;
    selRow = row;

    updateCell(oldRow, oldCol);
    updateCell(selRow, selCol);
    if (row >= 0)
        emit selected(row, col);

#if QT_CONFIG(menu)
    if (isVisible() && qobject_cast<QMenu*>(parentWidget()))
        parentWidget()->close();
#endif
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 233, as _ZN10QWellArray9paintCellEP8QPainteriiRK5QRect
inline void QWellArray::paintCell(QPainter* p, int row, int col, const QRect &rect)
{
    int b = 3; //margin

    const QPalette & g = palette();
    QStyleOptionFrame opt;
    opt.initFrom(this);
    int dfw = style()->pixelMetric(QStyle::PM_DefaultFrameWidth, &opt, this);
    opt.lineWidth = dfw;
    opt.midLineWidth = 1;
    opt.rect = rect.adjusted(b, b, -b, -b);
    opt.palette = g;
    opt.state = QStyle::State_Enabled | QStyle::State_Sunken;
    style()->drawPrimitive(QStyle::PE_Frame, &opt, p, this);
    b += dfw;

    if ((row == curRow) && (col == curCol)) {
        if (hasFocus()) {
            QStyleOptionFocusRect opt;
            opt.palette = g;
            opt.rect = rect;
            opt.state = QStyle::State_None | QStyle::State_KeyboardFocusChange;
            style()->drawPrimitive(QStyle::PE_FrameFocusRect, &opt, p, this);
        }
    }
    paintCellContents(p, row, col, opt.rect.adjusted(dfw, dfw, -dfw, -dfw));
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 264, as _ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect
inline void QWellArray::paintCellContents(QPainter *p, int row, int col, const QRect &r)
{
    Q_UNUSED(row);
    Q_UNUSED(col);
    p->fillRect(r, Qt::white);
    p->setPen(Qt::black);
    p->drawLine(r.topLeft(), r.bottomRight());
    p->drawLine(r.topRight(), r.bottomLeft());
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 226, as _ZNK10QWellArray8sizeHintEv
inline QSize QWellArray::sizeHint() const
{
    ensurePolished();
    return gridSize().boundedTo(QSize(640, 480));
}

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

//  from src/widgets/dialogs/qcolordialog.cpp, line 355, as _ZN10QWellArray13keyPressEventEP9QKeyEvent
inline void QWellArray::keyPressEvent(QKeyEvent* e)
{
    switch(e->key()) {                        // Look at the key code
    case Qt::Key_Left:                                // If 'left arrow'-key,
        if (curCol > 0)                        // and cr't not in leftmost col
            setCurrent(curRow, curCol - 1);        // set cr't to next left column
        break;
    case Qt::Key_Right:                                // Correspondingly...
        if (curCol < numCols()-1)
            setCurrent(curRow, curCol + 1);
        break;
    case Qt::Key_Up:
        if (curRow > 0)
            setCurrent(curRow - 1, curCol);
        break;
    case Qt::Key_Down:
        if (curRow < numRows()-1)
            setCurrent(curRow + 1, curCol);
        break;
    case Qt::Key_Space:
        setSelected(curRow, curCol);
        break;
    default:                                // If not an interesting key,
        e->ignore();                        // we don't accept the event
        return;
    }
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 342, as _ZN10QWellArray12focusInEventEP11QFocusEvent
inline void QWellArray::focusInEvent(QFocusEvent*)
{
    updateCell(curRow, curCol);
    emit currentChanged(curRow, curCol);
    sendAccessibleChildFocusEvent();
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 350, as _ZN10QWellArray13focusOutEventEP11QFocusEvent
inline void QWellArray::focusOutEvent(QFocusEvent*)
{
    updateCell(curRow, curCol);
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 166, as _ZN10QWellArray10paintEventEP11QPaintEvent
inline void QWellArray::paintEvent(QPaintEvent *e)
{
    QRect r = e->rect();
    int cx = r.x();
    int cy = r.y();
    int ch = r.height();
    int cw = r.width();
    int colfirst = columnAt(cx);
    int collast = columnAt(cx + cw);
    int rowfirst = rowAt(cy);
    int rowlast = rowAt(cy + ch);

    if (isRightToLeft()) {
        int t = colfirst;
        colfirst = collast;
        collast = t;
    }

    QPainter painter(this);
    QPainter *p = &painter;
    QRect rect(0, 0, cellWidth(), cellHeight());


    if (collast < 0 || collast >= ncols)
        collast = ncols-1;
    if (rowlast < 0 || rowlast >= nrows)
        rowlast = nrows-1;

    // Go through the rows
    for (int r = rowfirst; r <= rowlast; ++r) {
        // get row position and height
        int rowp = rowY(r);

        // Go through the columns in the row r
        // if we know from where to where, go through [colfirst, collast],
        // else go through all of them
        for (int c = colfirst; c <= collast; ++c) {
            // get position and width of column c
            int colp = columnX(c);
            // Translate painter and draw the cell
            rect.translate(colp, rowp);
            paintCell(p, r, c, rect);
            rect.translate(-colp, -rowp);
        }
    }
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 383, as _ZN10QWellArray29sendAccessibleChildFocusEventEv
inline void QWellArray::sendAccessibleChildFocusEvent()
{
#if QT_CONFIG(accessibility)
    if (!QAccessible::isActive())
        return;

    if (hasFocus() && curRow >= 0 && curCol >= 0) {
        const int itemIndex = index(curRow, curCol);
        QAccessibleEvent event(this, QAccessible::Focus);
        event.setChild(itemIndex);
        QAccessible::updateAccessibility(&event);
    }
#endif
}
//  -----------------------------------------------------------------------

//  Only a class built on QWellArray may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWellArray : QWellArray {
  using QWellArray::paintCell;
  using QWellArray::paintCellContents;
  using QWellArray::mousePressEvent;
  using QWellArray::mouseReleaseEvent;
  using QWellArray::keyPressEvent;
  using QWellArray::focusOutEvent;
  using QWellArray::paintEvent;
};

//  A QWellArray that Python can take functions over in. Every QWellArray
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWellArrayCall0)(const void *, int, int, int *);
typedef void (*CuteQWellArrayCall1)(const void *, int, int, int *);
typedef const QSize * (*CuteQWellArrayCall2)(const void *, int *);
typedef void (*CuteQWellArrayCall3)(const void *, QPainter *, int, int, const QRect *, int *);
typedef void (*CuteQWellArrayCall4)(const void *, QPainter *, int, int, const QRect *, int *);
typedef void (*CuteQWellArrayCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWellArrayCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWellArrayCall7)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWellArrayCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWellArrayCall9)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWellArrayCall10)(const void *, QPaintEvent *, int *);
typedef int (*CuteQWellArrayCall11)(const void *, int *);
typedef void (*CuteQWellArrayCall12)(const void *, bool, int *);
typedef const QSize * (*CuteQWellArrayCall13)(const void *, int *);
typedef int (*CuteQWellArrayCall14)(const void *, int, int *);
typedef bool (*CuteQWellArrayCall15)(const void *, int *);
typedef void * (*CuteQWellArrayCall16)(const void *, int *);
typedef bool (*CuteQWellArrayCall17)(const void *, QEvent *, int *);
typedef void (*CuteQWellArrayCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWellArrayCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWellArrayCall20)(const void *, QWheelEvent *, int *);
typedef void (*CuteQWellArrayCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWellArrayCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWellArrayCall23)(const void *, QEvent *, int *);
typedef void (*CuteQWellArrayCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWellArrayCall25)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWellArrayCall26)(const void *, QCloseEvent *, int *);
typedef void (*CuteQWellArrayCall27)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQWellArrayCall28)(const void *, QTabletEvent *, int *);
typedef void (*CuteQWellArrayCall29)(const void *, QActionEvent *, int *);
typedef void (*CuteQWellArrayCall30)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQWellArrayCall31)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQWellArrayCall32)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQWellArrayCall33)(const void *, QDropEvent *, int *);
typedef void (*CuteQWellArrayCall34)(const void *, QShowEvent *, int *);
typedef void (*CuteQWellArrayCall35)(const void *, QHideEvent *, int *);
typedef void (*CuteQWellArrayCall36)(const void *, QEvent *, int *);
typedef int (*CuteQWellArrayCall37)(const void *, int, int *);
typedef void (*CuteQWellArrayCall38)(const void *, QPainter *, int *);
typedef void * (*CuteQWellArrayCall39)(const void *, QPoint *, int *);
typedef void * (*CuteQWellArrayCall40)(const void *, int *);
typedef void (*CuteQWellArrayCall41)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQWellArrayCall42)(const void *, int, int *);
typedef bool (*CuteQWellArrayCall43)(const void *, bool, int *);
typedef bool (*CuteQWellArrayCall44)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQWellArrayCall45)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWellArrayCall46)(const void *, QChildEvent *, int *);
typedef void (*CuteQWellArrayCall47)(const void *, QEvent *, int *);
typedef void (*CuteQWellArrayCall48)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWellArrayCall49)(const void *, const QMetaMethod *, int *);
class CuteQWellArray : public QWellArray {
public:
  using QWellArray::QWellArray;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QWellArray10setCurrentEii")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QWellArray11setSelectedEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    return false;
  }

  //  void QWellArray::setCurrent(int row, int col)
  void setCurrent(int row, int col) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWellArrayCall0 call = reinterpret_cast<CuteQWellArrayCall0>(taken[0]);
      call(this, row, col, &handled);
      if (handled) return;
    }
    QWellArray::setCurrent(row, col);
  }

  //  void QWellArray::setSelected(int row, int col)
  void setSelected(int row, int col) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWellArrayCall1 call = reinterpret_cast<CuteQWellArrayCall1>(taken[1]);
      call(this, row, col, &handled);
      if (handled) return;
    }
    QWellArray::setSelected(row, col);
  }

  //  QSize QWellArray::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWellArrayCall2 call = reinterpret_cast<CuteQWellArrayCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWellArray::sizeHint();
  }

  //  void QWellArray::paintCell(QPainter *a0, int row, int col, const
  //      QRect &a3)
  void paintCell(QPainter *a0, int row, int col, const QRect &a3) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWellArrayCall3 call = reinterpret_cast<CuteQWellArrayCall3>(taken[3]);
      call(this, a0, row, col, &a3, &handled);
      if (handled) return;
    }
    QWellArray::paintCell(a0, row, col, a3);
  }

  //  void QWellArray::paintCellContents(QPainter *a0, int row, int col,
  //      const QRect &a3)
  void paintCellContents(
      QPainter *a0,
      int row,
      int col,
      const QRect &a3) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWellArrayCall4 call = reinterpret_cast<CuteQWellArrayCall4>(taken[4]);
      call(this, a0, row, col, &a3, &handled);
      if (handled) return;
    }
    QWellArray::paintCellContents(a0, row, col, a3);
  }

  //  void QWellArray::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWellArrayCall5 call = reinterpret_cast<CuteQWellArrayCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWellArray::mousePressEvent(a0);
  }

  //  void QWellArray::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWellArrayCall6 call = reinterpret_cast<CuteQWellArrayCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWellArray::mouseReleaseEvent(a0);
  }

  //  void QWellArray::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWellArrayCall7 call = reinterpret_cast<CuteQWellArrayCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWellArray::keyPressEvent(a0);
  }

  //  void QWellArray::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWellArrayCall8 call = reinterpret_cast<CuteQWellArrayCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWellArray::focusInEvent(a0);
  }

  //  void QWellArray::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWellArrayCall9 call = reinterpret_cast<CuteQWellArrayCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWellArray::focusOutEvent(a0);
  }

  //  void QWellArray::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWellArrayCall10 call = reinterpret_cast<CuteQWellArrayCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWellArray::paintEvent(a0);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWellArrayCall11 call = reinterpret_cast<CuteQWellArrayCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWellArrayCall12 call = reinterpret_cast<CuteQWellArrayCall12>(taken[12]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQWellArrayCall13 call = reinterpret_cast<CuteQWellArrayCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQWellArrayCall14 call = reinterpret_cast<CuteQWellArrayCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQWellArrayCall15 call = reinterpret_cast<CuteQWellArrayCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQWellArrayCall16 call = reinterpret_cast<CuteQWellArrayCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWellArrayCall17 call = reinterpret_cast<CuteQWellArrayCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWellArrayCall18 call = reinterpret_cast<CuteQWellArrayCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWellArrayCall19 call = reinterpret_cast<CuteQWellArrayCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWellArrayCall20 call = reinterpret_cast<CuteQWellArrayCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWellArrayCall21 call = reinterpret_cast<CuteQWellArrayCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWellArrayCall22 call = reinterpret_cast<CuteQWellArrayCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWellArrayCall23 call = reinterpret_cast<CuteQWellArrayCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWellArrayCall24 call = reinterpret_cast<CuteQWellArrayCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWellArrayCall25 call = reinterpret_cast<CuteQWellArrayCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWellArrayCall26 call = reinterpret_cast<CuteQWellArrayCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWellArrayCall27 call = reinterpret_cast<CuteQWellArrayCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWellArrayCall28 call = reinterpret_cast<CuteQWellArrayCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWellArrayCall29 call = reinterpret_cast<CuteQWellArrayCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWellArrayCall30 call = reinterpret_cast<CuteQWellArrayCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWellArrayCall31 call = reinterpret_cast<CuteQWellArrayCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWellArrayCall32 call = reinterpret_cast<CuteQWellArrayCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQWellArrayCall33 call = reinterpret_cast<CuteQWellArrayCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQWellArrayCall34 call = reinterpret_cast<CuteQWellArrayCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQWellArrayCall35 call = reinterpret_cast<CuteQWellArrayCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQWellArrayCall36 call = reinterpret_cast<CuteQWellArrayCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQWellArrayCall37 call = reinterpret_cast<CuteQWellArrayCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQWellArrayCall38 call = reinterpret_cast<CuteQWellArrayCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQWellArrayCall39 call = reinterpret_cast<CuteQWellArrayCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQWellArrayCall40 call = reinterpret_cast<CuteQWellArrayCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQWellArrayCall41 call = reinterpret_cast<CuteQWellArrayCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQWellArrayCall42 call = reinterpret_cast<CuteQWellArrayCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      CuteQWellArrayCall43 call = reinterpret_cast<CuteQWellArrayCall43>(taken[43]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQWellArrayCall44 call = reinterpret_cast<CuteQWellArrayCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQWellArrayCall45 call = reinterpret_cast<CuteQWellArrayCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQWellArrayCall46 call = reinterpret_cast<CuteQWellArrayCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQWellArrayCall47 call = reinterpret_cast<CuteQWellArrayCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQWellArrayCall48 call = reinterpret_cast<CuteQWellArrayCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQWellArrayCall49 call = reinterpret_cast<CuteQWellArrayCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QWellArray::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QWellArray10metaObjectEv(
    const QWellArray *self) {
  return self->metaObject();
}

//  QWellArray::~QWellArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArrayD1Ev(QWellArray *self) {
  delete self;
}

//  int QWellArray::currentColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray13currentColumnEv(const QWellArray *self) {
  return self->currentColumn();
}

//  int QWellArray::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray10currentRowEv(const QWellArray *self) {
  return self->currentRow();
}

//  int QWellArray::selectedColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray14selectedColumnEv(const QWellArray *self) {
  return self->selectedColumn();
}

//  int QWellArray::selectedRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray11selectedRowEv(const QWellArray *self) {
  return self->selectedRow();
}

//  void QWellArray::setCurrent(int row, int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray10setCurrentEii(
    QWellArray *self,
    int row,
    int col) {
  self->setCurrent(row, col);
}

//  void QWellArray::setSelected(int row, int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray11setSelectedEii(
    QWellArray *self,
    int row,
    int col) {
  self->setSelected(row, col);
}

//  QSize QWellArray::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QWellArray8sizeHintEv(const QWellArray *self) {
  return new QSize(self->sizeHint());
}

//  int QWellArray::cellWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray9cellWidthEv(const QWellArray *self) {
  return self->cellWidth();
}

//  int QWellArray::cellHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray10cellHeightEv(const QWellArray *self) {
  return self->cellHeight();
}

//  int QWellArray::rowAt(int y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray5rowAtEi(const QWellArray *self, int y) {
  return self->rowAt(y);
}

//  int QWellArray::columnAt(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray8columnAtEi(const QWellArray *self, int x) {
  return self->columnAt(x);
}

//  int QWellArray::rowY(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray4rowYEi(const QWellArray *self, int row) {
  return self->rowY(row);
}

//  int QWellArray::columnX(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray7columnXEi(const QWellArray *self, int column) {
  return self->columnX(column);
}

//  int QWellArray::numRows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray7numRowsEv(const QWellArray *self) {
  return self->numRows();
}

//  int QWellArray::numCols() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWellArray7numColsEv(const QWellArray *self) {
  return self->numCols();
}

//  int QWellArray::index(int row, int col)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QWellArray5indexEii(QWellArray *self, int row, int col) {
  return self->index(row, col);
}

//  QRect QWellArray::cellRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10QWellArray8cellRectEv(const QWellArray *self) {
  return new QRect(self->cellRect());
}

//  QSize QWellArray::gridSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QWellArray8gridSizeEv(const QWellArray *self) {
  return new QSize(self->gridSize());
}

//  QRect QWellArray::cellGeometry(int row, int column)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN10QWellArray12cellGeometryEii(
    QWellArray *self,
    int row,
    int column) {
  return new QRect(self->cellGeometry(row, column));
}

//  void QWellArray::updateCell(int row, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray10updateCellEii(
    QWellArray *self,
    int row,
    int column) {
  self->updateCell(row, column);
}

//  void QWellArray::paintCell(QPainter *a0, int row, int col, const QRect
//      &a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect(
    QWellArray *self,
    QPainter *a0,
    int row,
    int col,
    const QRect *a3) {
  self->paintCell(a0, row, col, *a3);
}

//  void QWellArray::paintCellContents(QPainter *a0, int row, int col, const
//      QRect &a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect(
    QWellArray *self,
    QPainter *a0,
    int row,
    int col,
    const QRect *a3) {
  self->paintCellContents(a0, row, col, *a3);
}

//  void QWellArray::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray15mousePressEventEP11QMouseEvent(
    QWellArray *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QWellArray::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray17mouseReleaseEventEP11QMouseEvent(
    QWellArray *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QWellArray::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray13keyPressEventEP9QKeyEvent(
    QWellArray *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QWellArray::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray12focusInEventEP11QFocusEvent(
    QWellArray *self,
    QFocusEvent *a0) {
  self->focusInEvent(a0);
}

//  void QWellArray::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray13focusOutEventEP11QFocusEvent(
    QWellArray *self,
    QFocusEvent *a0) {
  self->focusOutEvent(a0);
}

//  void QWellArray::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray10paintEventEP11QPaintEvent(
    QWellArray *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QWellArray::sendAccessibleChildFocusEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray29sendAccessibleChildFocusEventEv(
    QWellArray *self) {
  self->sendAccessibleChildFocusEvent();
}

//  a Python function taken by a CuteQWellArray, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWellArray(QWellArray *self, const char *key, void *call) {
  return static_cast<CuteQWellArray *>(self)->take(key, call);
}

//  QSize QWellArray::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QWellArray8sizeHintEv(const QWellArray *self) {
  return new QSize(self->QWellArray::sizeHint());
}

//  void QWellArray::paintCell(QPainter *a0, int row, int col, const QRect
//      &a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect(
    QWellArray *self,
    QPainter *a0,
    int row,
    int col,
    const QRect *a3) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::paintCell(
      a0,
      row,
      col,
      *a3);
}

//  void QWellArray::paintCellContents(QPainter *a0, int row, int col, const
//      QRect &a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect(
    QWellArray *self,
    QPainter *a0,
    int row,
    int col,
    const QRect *a3) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::paintCellContents(
      a0,
      row,
      col,
      *a3);
}

//  void QWellArray::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray15mousePressEventEP11QMouseEvent(
    QWellArray *self,
    QMouseEvent *a0) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::mousePressEvent(a0);
}

//  void QWellArray::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray17mouseReleaseEventEP11QMouseEvent(
    QWellArray *self,
    QMouseEvent *a0) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::mouseReleaseEvent(a0);
}

//  void QWellArray::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray13keyPressEventEP9QKeyEvent(
    QWellArray *self,
    QKeyEvent *a0) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::keyPressEvent(a0);
}

//  void QWellArray::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray13focusOutEventEP11QFocusEvent(
    QWellArray *self,
    QFocusEvent *a0) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::focusOutEvent(a0);
}

//  void QWellArray::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray10paintEventEP11QPaintEvent(
    QWellArray *self,
    QPaintEvent *a0) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::paintEvent(a0);
}
