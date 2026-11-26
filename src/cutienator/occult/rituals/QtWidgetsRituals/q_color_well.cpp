//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QColorWell' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 3 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/qcolordialog.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qimage.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qlineedit.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtGui/qpainter.h>
#include <QtGui/qpixmap.h>
#include <QtWidgets/qpushbutton.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#if QT_CONFIG(settings)
#include <QtCore/qsettings.h>
#endif
#include <QtCore/qsharedpointer.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qvalidator.h>
#include <QtCore/qmimedata.h>
#include <QtWidgets/qspinbox.h>
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtGui/qscreen.h>
#include <QtGui/qcursor.h>
#include <QtCore/qtimer.h>
#include <QtGui/qwindow.h>
#include <QtWidgets/private/qdialog_p.h>
#include <QtWidgets/private/qcolorwell_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformservices.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/qpointer.h>
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

using namespace Qt::StringLiterals;

//  from QtWidgets__QColorWell.cpp, line 1, as moc:QColorWell
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN10QColorWellE_t {};
} // unnamed namespace

template <> constexpr inline auto QColorWell::qt_create_metaobjectdata<qt_meta_tag_ZN10QColorWellE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QColorWell"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QColorWell, qt_meta_tag_ZN10QColorWellE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QColorWell::staticMetaObject = { {
    QMetaObject::SuperData::link<QWellArray::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10QColorWellE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10QColorWellE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN10QColorWellE_t>.metaTypes,
    nullptr
} };

void QColorWell::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QColorWell *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QColorWell::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QColorWell::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10QColorWellE_t>.strings))
        return static_cast<void*>(this);
    return QWellArray::qt_metacast(_clname);
}

int QColorWell::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWellArray::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

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

//  from src/widgets/dialogs/qcolordialog.cpp, line 528, as _ZN10QColorWell15mousePressEventEP11QMouseEvent
inline void QColorWell::mousePressEvent(QMouseEvent *e)
{
    oldCurrent = QPoint(selectedRow(), selectedColumn());
    QWellArray::mousePressEvent(e);
    mousePressed = true;
    pressPos = e->position().toPoint();
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 601, as _ZN10QColorWell17mouseReleaseEventEP11QMouseEvent
inline void QColorWell::mouseReleaseEvent(QMouseEvent *e)
{
    if (!mousePressed)
        return;
    QWellArray::mouseReleaseEvent(e);
    mousePressed = false;
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 522, as _ZN10QColorWell17paintCellContentsEP8QPainteriiRK5QRect
inline void QColorWell::paintCellContents(QPainter *p, int row, int col, const QRect &r)
{
    int i = row + col*numRows();
    p->fillRect(r, QColor(values[i]));
}

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

//  from src/widgets/dialogs/qcolordialog.cpp, line 226, as _ZNK10QWellArray8sizeHintEv
inline QSize QWellArray::sizeHint() const
{
    ensurePolished();
    return gridSize().boundedTo(QSize(640, 480));
}

//  from src/widgets/dialogs/qcolordialog.cpp, line 213, as _ZN10QWellArrayC2EiiP7QWidget
inline QWellArray::QWellArray(int rows, int cols, QWidget *parent)
    : QWidget(parent)
        ,nrows(rows), ncols(cols)
{
    setFocusPolicy(Qt::StrongFocus);
    cellw = 28;
    cellh = 24;
    curCol = 0;
    curRow = 0;
    selCol = -1;
    selRow = -1;
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
  using QColorWell::dropEvent;
};

//  const QMetaObject *QColorWell::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QColorWell10metaObjectEv(
    const QColorWell *self) {
  return self->metaObject();
}

//  void *QColorWell::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QColorWell11qt_metacastEPKc(
    QColorWell *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QColorWell::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QColorWell11qt_metacallEN11QMetaObject4CallEiPPv(
    QColorWell *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QColorWell::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QColorWell2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColorWell::tr(s, c, n));
}

#if QT_CONFIG(draganddrop)
//  QColorWell::QColorWell(QWidget *parent, int r, int c, const QRgb *vals)
extern "C" Q_DECL_EXPORT
QColorWell *ritual_ZN10QColorWellC1EP7QWidgetiiPKj(
    QWidget *parent,
    int r,
    int c,
    const QRgb *vals) {
  return new QColorWell(parent, r, c, vals);
}
#endif  // QT_CONFIG(draganddrop)

//  const QRgb *QColorWell::rgbValues()
extern "C" Q_DECL_EXPORT
const QRgb *ritual_ZN10QColorWell9rgbValuesEv(QColorWell *self) {
  return self->rgbValues();
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

#if QT_CONFIG(draganddrop)
//  void QColorWell::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QColorWell9dropEventEP10QDropEvent(
    QColorWell *self,
    QDropEvent *e) {
  static_cast<OwnQColorWell *>(self)->OwnQColorWell::dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#endif  // QT_CONFIG(colordialog)
#endif  // QT_CONFIG(colordialog)
