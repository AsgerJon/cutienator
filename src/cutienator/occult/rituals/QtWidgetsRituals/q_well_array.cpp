//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QWellArray' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 5 rituals that lean on what moc writes for
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
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtWidgets__QWellArray.cpp, line 1, as moc:QWellArray
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN10QWellArrayE_t {};
} // unnamed namespace

template <> constexpr inline auto QWellArray::qt_create_metaobjectdata<qt_meta_tag_ZN10QWellArrayE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QWellArray",
        "selected",
        "",
        "row",
        "col",
        "currentChanged",
        "colorChanged",
        "index",
        "QRgb",
        "color",
        "selectedColumn",
        "selectedRow"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'selected'
        QtMocHelpers::SignalData<void(int, int)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 3 }, { QMetaType::Int, 4 },
        }}),
        // Signal 'currentChanged'
        QtMocHelpers::SignalData<void(int, int)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 3 }, { QMetaType::Int, 4 },
        }}),
        // Signal 'colorChanged'
        QtMocHelpers::SignalData<void(int, QRgb)>(6, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 7 }, { 0x80000000 | 8, 9 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'selectedColumn'
        QtMocHelpers::PropertyData<int>(10, QMetaType::Int, QMC::DefaultPropertyFlags),
        // property 'selectedRow'
        QtMocHelpers::PropertyData<int>(11, QMetaType::Int, QMC::DefaultPropertyFlags),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QWellArray, qt_meta_tag_ZN10QWellArrayE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QWellArray::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10QWellArrayE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10QWellArrayE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN10QWellArrayE_t>.metaTypes,
    nullptr
} };

void QWellArray::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QWellArray *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->selected((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2]))); break;
        case 1: _t->currentChanged((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2]))); break;
        case 2: _t->colorChanged((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QRgb>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QWellArray::*)(int , int )>(_a, &QWellArray::selected, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWellArray::*)(int , int )>(_a, &QWellArray::currentChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWellArray::*)(int , QRgb )>(_a, &QWellArray::colorChanged, 2))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<int*>(_v) = _t->selectedColumn(); break;
        case 1: *reinterpret_cast<int*>(_v) = _t->selectedRow(); break;
        default: break;
        }
    }
}

const QMetaObject *QWellArray::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QWellArray::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10QWellArrayE_t>.strings))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QWellArray::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void QWellArray::selected(int _t1, int _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1, _t2);
}

// SIGNAL 1
void QWellArray::currentChanged(int _t1, int _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1, _t2);
}

// SIGNAL 2
void QWellArray::colorChanged(int _t1, QRgb _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1, _t2);
}
QT_WARNING_POP

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

//  from src/widgets/dialogs/qcolordialog.cpp, line 213, as _ZN10QWellArrayC1EiiP7QWidget
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
  using QWellArray::focusInEvent;
  using QWellArray::focusOutEvent;
  using QWellArray::paintEvent;
};

//  A QWellArray that Python can take functions over in. Every QWellArray
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef const QSize * (*CuteQWellArrayCall2)(const void *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall3)(const void *, QPainter *, int, int, const QRect *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall4)(const void *, QPainter *, int, int, const QRect *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall6)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall7)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall8)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall9)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
typedef void (*CuteQWellArrayCall10)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(colordialog)
typedef int (*CuteQWellArrayCall11)(const void *, int *);
typedef void (*CuteQWellArrayCall12)(const void *, bool, int *);
typedef const QSize * (*CuteQWellArrayCall13)(const void *, int *);
typedef int (*CuteQWellArrayCall14)(const void *, int, int *);
typedef bool (*CuteQWellArrayCall15)(const void *, int *);
typedef void * (*CuteQWellArrayCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWellArrayCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWellArrayCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWellArrayCall19)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWellArrayCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWellArrayCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWellArrayCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWellArrayCall23)(const void *, QEvent *, int *);
typedef void (*CuteQWellArrayCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWellArrayCall25)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWellArrayCall26)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQWellArrayCall27)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQWellArrayCall28)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQWellArrayCall29)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWellArrayCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWellArrayCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWellArrayCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWellArrayCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
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
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWellArrayCall44)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWellArrayCall45)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWellArrayCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWellArrayCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWellArrayCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWellArrayCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWellArray : public QWellArray {
public:
  using QWellArray::QWellArray;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN10QWellArray10setCurrentEii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN10QWellArray11setSelectedEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
#if QT_CONFIG(colordialog)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(colordialog)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

#if QT_CONFIG(colordialog)
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
#endif  // QT_CONFIG(colordialog)

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

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

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

#if QT_CONFIG(wheelevent)
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
#endif  // QT_CONFIG(wheelevent)

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

#if !defined(QT_NO_CONTEXTMENU)
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
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
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
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
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
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
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
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
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
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
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
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
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
#endif  // QT_CONFIG(draganddrop)

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

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWellArray::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QWellArray10metaObjectEv(
    const QWellArray *self) {
  return self->metaObject();
}

//  void *QWellArray::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QWellArray11qt_metacastEPKc(
    QWellArray *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWellArray::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QWellArray11qt_metacallEN11QMetaObject4CallEiPPv(
    QWellArray *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWellArray::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QWellArray2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWellArray::tr(s, c, n));
}

//  QWellArray::QWellArray(int rows, int cols, QWidget *parent)
extern "C" Q_DECL_EXPORT
QWellArray *ritual_ZN10QWellArrayC1EiiP7QWidget(
    int rows,
    int cols,
    QWidget *parent) {
  return new CuteQWellArray(rows, cols, parent);
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

//  void QWellArray::selected(int row, int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray8selectedEii(QWellArray *self, int row, int col) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWellArray")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selected(int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selected(int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&row)),
      const_cast<void *>(static_cast<const void *>(&col)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWellArray::currentChanged(int row, int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWellArray14currentChangedEii(
    QWellArray *self,
    int row,
    int col) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWellArray")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentChanged(int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentChanged(int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&row)),
      const_cast<void *>(static_cast<const void *>(&col)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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

//  void QWellArray::setCurrent(int row, int col)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray10setCurrentEii(
    QWellArray *self,
    int row,
    int col) {
  self->QWellArray::setCurrent(row, col);
}

//  void QWellArray::setSelected(int row, int col)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray11setSelectedEii(
    QWellArray *self,
    int row,
    int col) {
  self->QWellArray::setSelected(row, col);
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

//  void QWellArray::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QWellArray12focusInEventEP11QFocusEvent(
    QWellArray *self,
    QFocusEvent *a0) {
  static_cast<OwnQWellArray *>(self)->OwnQWellArray::focusInEvent(a0);
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

#endif  // QT_CONFIG(colordialog)
#endif  // QT_CONFIG(colordialog)
