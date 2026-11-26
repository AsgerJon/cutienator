//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/properties_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QAbstractFormBuilderGadget' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/properties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDesigner__QAbstractFormBuilderGadget.cpp, line 1, as moc:QAbstractFormBuilderGadget
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t {};
} // unnamed namespace

template <> constexpr inline auto QAbstractFormBuilderGadget::qt_create_metaobjectdata<qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QAbstractFormBuilderGadget",
        "itemFlags",
        "Qt::ItemFlags",
        "checkState",
        "Qt::CheckState",
        "textAlignment",
        "Qt::Alignment",
        "orientation",
        "Qt::Orientation",
        "sizeType",
        "QSizePolicy::Policy",
        "colorRole",
        "QPalette::ColorRole",
        "colorGroup",
        "QPalette::ColorGroup",
        "styleStrategy",
        "QFont::StyleStrategy",
        "hintingPreference",
        "QFont::HintingPreference",
        "fontWeight",
        "QFont::Weight",
        "cursorShape",
        "Qt::CursorShape",
        "brushStyle",
        "Qt::BrushStyle",
        "toolBarArea",
        "Qt::ToolBarArea",
        "gradientType",
        "QGradient::Type",
        "gradientSpread",
        "QGradient::Spread",
        "gradientCoordinate",
        "QGradient::CoordinateMode",
        "language",
        "QLocale::Language",
        "country",
        "QLocale::Country"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
        // property 'itemFlags'
        QtMocHelpers::PropertyData<Qt::ItemFlags>(1, 0x80000000 | 2, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'checkState'
        QtMocHelpers::PropertyData<Qt::CheckState>(3, 0x80000000 | 4, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'textAlignment'
        QtMocHelpers::PropertyData<Qt::Alignment>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'orientation'
        QtMocHelpers::PropertyData<Qt::Orientation>(7, 0x80000000 | 8, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'sizeType'
        QtMocHelpers::PropertyData<QSizePolicy::Policy>(9, 0x80000000 | 10, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'colorRole'
        QtMocHelpers::PropertyData<QPalette::ColorRole>(11, 0x80000000 | 12, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'colorGroup'
        QtMocHelpers::PropertyData<QPalette::ColorGroup>(13, 0x80000000 | 14, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'styleStrategy'
        QtMocHelpers::PropertyData<QFont::StyleStrategy>(15, 0x80000000 | 16, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'hintingPreference'
        QtMocHelpers::PropertyData<QFont::HintingPreference>(17, 0x80000000 | 18, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'fontWeight'
        QtMocHelpers::PropertyData<QFont::Weight>(19, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'cursorShape'
        QtMocHelpers::PropertyData<Qt::CursorShape>(21, 0x80000000 | 22, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'brushStyle'
        QtMocHelpers::PropertyData<Qt::BrushStyle>(23, 0x80000000 | 24, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'toolBarArea'
        QtMocHelpers::PropertyData<Qt::ToolBarArea>(25, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'gradientType'
        QtMocHelpers::PropertyData<QGradient::Type>(27, 0x80000000 | 28, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'gradientSpread'
        QtMocHelpers::PropertyData<QGradient::Spread>(29, 0x80000000 | 30, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'gradientCoordinate'
        QtMocHelpers::PropertyData<QGradient::CoordinateMode>(31, 0x80000000 | 32, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'language'
        QtMocHelpers::PropertyData<QLocale::Language>(33, 0x80000000 | 34, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'country'
        QtMocHelpers::PropertyData<QLocale::Country>(35, 0x80000000 | 36, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QAbstractFormBuilderGadget, qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT static const QMetaObject::SuperData qt_meta_extradata_ZN26QAbstractFormBuilderGadgetE[] = {
    QMetaObject::SuperData::link<QSizePolicy::staticMetaObject>(),
    QMetaObject::SuperData::link<QPalette::staticMetaObject>(),
    QMetaObject::SuperData::link<QFont::staticMetaObject>(),
    QMetaObject::SuperData::link<QGradient::staticMetaObject>(),
    QMetaObject::SuperData::link<QLocale::staticMetaObject>(),
    nullptr
};

Q_CONSTINIT const QMetaObject QAbstractFormBuilderGadget::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t>.data,
    qt_static_metacall,
    qt_meta_extradata_ZN26QAbstractFormBuilderGadgetE,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t>.metaTypes,
    nullptr
} };

void QAbstractFormBuilderGadget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QAbstractFormBuilderGadget *>(_o);
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<Qt::ItemFlags*>(_v) = _t->fakeItemFlags(); break;
        case 1: *reinterpret_cast<Qt::CheckState*>(_v) = _t->fakeCheckState(); break;
        case 2: *reinterpret_cast<Qt::Alignment*>(_v) = _t->fakeAlignment(); break;
        case 3: *reinterpret_cast<Qt::Orientation*>(_v) = _t->fakeOrientation(); break;
        case 4: *reinterpret_cast<QSizePolicy::Policy*>(_v) = _t->fakeSizeType(); break;
        case 5: *reinterpret_cast<QPalette::ColorRole*>(_v) = _t->fakeColorRole(); break;
        case 6: *reinterpret_cast<QPalette::ColorGroup*>(_v) = _t->fakeColorGroup(); break;
        case 7: *reinterpret_cast<QFont::StyleStrategy*>(_v) = _t->fakeStyleStrategy(); break;
        case 8: *reinterpret_cast<QFont::HintingPreference*>(_v) = _t->fakeHintingPreference(); break;
        case 9: *reinterpret_cast<QFont::Weight*>(_v) = _t->fakeFontWeight(); break;
        case 10: *reinterpret_cast<Qt::CursorShape*>(_v) = _t->fakeCursorShape(); break;
        case 11: *reinterpret_cast<Qt::BrushStyle*>(_v) = _t->fakeBrushStyle(); break;
        case 12: *reinterpret_cast<Qt::ToolBarArea*>(_v) = _t->fakeToolBarArea(); break;
        case 13: *reinterpret_cast<QGradient::Type*>(_v) = _t->fakeGradientType(); break;
        case 14: *reinterpret_cast<QGradient::Spread*>(_v) = _t->fakeGradientSpread(); break;
        case 15: *reinterpret_cast<QGradient::CoordinateMode*>(_v) = _t->fakeGradientCoordinate(); break;
        case 16: *reinterpret_cast<QLocale::Language*>(_v) = _t->fakeLanguage(); break;
        case 17: *reinterpret_cast<QLocale::Country*>(_v) = _t->fakeCountry(); break;
        default: break;
        }
    }
}

const QMetaObject *QAbstractFormBuilderGadget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QAbstractFormBuilderGadget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QAbstractFormBuilderGadgetE_t>.strings))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QAbstractFormBuilderGadget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 18;
    }
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  A QAbstractFormBuilderGadget that Python can take functions over in. Every QAbstractFormBuilderGadget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAbstractFormBuilderGadgetCall0)(const void *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall1)(const void *, bool, int *);
typedef const QSize * (*CuteQAbstractFormBuilderGadgetCall2)(const void *, int *);
typedef const QSize * (*CuteQAbstractFormBuilderGadgetCall3)(const void *, int *);
typedef int (*CuteQAbstractFormBuilderGadgetCall4)(const void *, int, int *);
typedef bool (*CuteQAbstractFormBuilderGadgetCall5)(const void *, int *);
typedef void * (*CuteQAbstractFormBuilderGadgetCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractFormBuilderGadgetCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractFormBuilderGadgetCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall11)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQAbstractFormBuilderGadgetCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQAbstractFormBuilderGadgetCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall17)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall18)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall19)(const void *, QPaintEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQAbstractFormBuilderGadgetCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAbstractFormBuilderGadgetCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQAbstractFormBuilderGadgetCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractFormBuilderGadgetCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractFormBuilderGadgetCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractFormBuilderGadgetCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractFormBuilderGadgetCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractFormBuilderGadgetCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQAbstractFormBuilderGadgetCall33)(const void *, int, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQAbstractFormBuilderGadgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQAbstractFormBuilderGadgetCall36)(const void *, int *);
typedef void (*CuteQAbstractFormBuilderGadgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQAbstractFormBuilderGadgetCall38)(const void *, int, int *);
typedef bool (*CuteQAbstractFormBuilderGadgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractFormBuilderGadgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractFormBuilderGadgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractFormBuilderGadgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractFormBuilderGadgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractFormBuilderGadgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractFormBuilderGadgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractFormBuilderGadget : public QAbstractFormBuilderGadget {
public:
  using QAbstractFormBuilderGadget::QAbstractFormBuilderGadget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[39] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall0 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall1 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall2 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall3 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall4 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall4>(taken[4]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall5 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall6 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall7 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall8 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall9 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall10 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall11 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall12 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall13 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall14 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall15 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall16 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall17 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall18 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall19 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall20 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall21 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall22 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall23 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall24 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall25 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall26 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall27 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall28 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall29 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall30 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall31 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall32 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall33 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall34 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall35 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall36 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall37 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall38 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall39 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall40 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall41 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall42 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall43 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall44 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQAbstractFormBuilderGadgetCall45 call = reinterpret_cast<CuteQAbstractFormBuilderGadgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractFormBuilderGadget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QAbstractFormBuilderGadget10metaObjectEv(
    const QAbstractFormBuilderGadget *self) {
  return self->metaObject();
}

//  void *QAbstractFormBuilderGadget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QAbstractFormBuilderGadget11qt_metacastEPKc(
    QAbstractFormBuilderGadget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractFormBuilderGadget::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QAbstractFormBuilderGadget11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractFormBuilderGadget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractFormBuilderGadget::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAbstractFormBuilderGadget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractFormBuilderGadget::tr(s, c, n));
}

//  QAbstractFormBuilderGadget::QAbstractFormBuilderGadget()
extern "C" Q_DECL_EXPORT
QAbstractFormBuilderGadget *ritual_ZN26QAbstractFormBuilderGadgetC1Ev() {
  return new CuteQAbstractFormBuilderGadget();
}

//  Qt::Orientation QAbstractFormBuilderGadget::fakeOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK26QAbstractFormBuilderGadget15fakeOrientationEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeOrientation();
}

//  QSizePolicy::Policy QAbstractFormBuilderGadget::fakeSizeType() const
extern "C" Q_DECL_EXPORT
QSizePolicy::Policy ritual_ZNK26QAbstractFormBuilderGadget12fakeSizeTypeEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeSizeType();
}

//  QPalette::ColorGroup QAbstractFormBuilderGadget::fakeColorGroup() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZNK26QAbstractFormBuilderGadget14fakeColorGroupEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeColorGroup();
}

//  QPalette::ColorRole QAbstractFormBuilderGadget::fakeColorRole() const
extern "C" Q_DECL_EXPORT
QPalette::ColorRole ritual_ZNK26QAbstractFormBuilderGadget13fakeColorRoleEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeColorRole();
}

//  QFont::StyleStrategy QAbstractFormBuilderGadget::fakeStyleStrategy()
//      const
extern "C" Q_DECL_EXPORT
QFont::StyleStrategy ritual_ZNK26QAbstractFormBuilderGadget17fakeStyleStrategyEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeStyleStrategy();
}

//  QFont::HintingPreference
//      QAbstractFormBuilderGadget::fakeHintingPreference() const
extern "C" Q_DECL_EXPORT
QFont::HintingPreference ritual_ZNK26QAbstractFormBuilderGadget21fakeHintingPreferenceEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeHintingPreference();
}

//  QFont::Weight QAbstractFormBuilderGadget::fakeFontWeight() const
extern "C" Q_DECL_EXPORT
QFont::Weight ritual_ZNK26QAbstractFormBuilderGadget14fakeFontWeightEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeFontWeight();
}

//  Qt::CursorShape QAbstractFormBuilderGadget::fakeCursorShape() const
extern "C" Q_DECL_EXPORT
Qt::CursorShape ritual_ZNK26QAbstractFormBuilderGadget15fakeCursorShapeEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeCursorShape();
}

//  Qt::BrushStyle QAbstractFormBuilderGadget::fakeBrushStyle() const
extern "C" Q_DECL_EXPORT
Qt::BrushStyle ritual_ZNK26QAbstractFormBuilderGadget14fakeBrushStyleEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeBrushStyle();
}

//  Qt::ToolBarArea QAbstractFormBuilderGadget::fakeToolBarArea() const
extern "C" Q_DECL_EXPORT
Qt::ToolBarArea ritual_ZNK26QAbstractFormBuilderGadget15fakeToolBarAreaEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeToolBarArea();
}

//  QGradient::Type QAbstractFormBuilderGadget::fakeGradientType() const
extern "C" Q_DECL_EXPORT
QGradient::Type ritual_ZNK26QAbstractFormBuilderGadget16fakeGradientTypeEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeGradientType();
}

//  QGradient::Spread QAbstractFormBuilderGadget::fakeGradientSpread() const
extern "C" Q_DECL_EXPORT
QGradient::Spread ritual_ZNK26QAbstractFormBuilderGadget18fakeGradientSpreadEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeGradientSpread();
}

//  QGradient::CoordinateMode
//      QAbstractFormBuilderGadget::fakeGradientCoordinate() const
extern "C" Q_DECL_EXPORT
QGradient::CoordinateMode ritual_ZNK26QAbstractFormBuilderGadget22fakeGradientCoordinateEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeGradientCoordinate();
}

//  QLocale::Language QAbstractFormBuilderGadget::fakeLanguage() const
extern "C" Q_DECL_EXPORT
QLocale::Language ritual_ZNK26QAbstractFormBuilderGadget12fakeLanguageEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeLanguage();
}

//  QLocale::Country QAbstractFormBuilderGadget::fakeCountry() const
extern "C" Q_DECL_EXPORT
QLocale::Country ritual_ZNK26QAbstractFormBuilderGadget11fakeCountryEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeCountry();
}

//  Qt::ItemFlags QAbstractFormBuilderGadget::fakeItemFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAbstractFormBuilderGadget13fakeItemFlagsEv(
    const QAbstractFormBuilderGadget *self) {
  return static_cast<int>(self->fakeItemFlags().toInt());
}

//  Qt::CheckState QAbstractFormBuilderGadget::fakeCheckState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK26QAbstractFormBuilderGadget14fakeCheckStateEv(
    const QAbstractFormBuilderGadget *self) {
  return self->fakeCheckState();
}

//  Qt::Alignment QAbstractFormBuilderGadget::fakeAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAbstractFormBuilderGadget13fakeAlignmentEv(
    const QAbstractFormBuilderGadget *self) {
  return static_cast<int>(self->fakeAlignment().toInt());
}

//  a Python function taken by a CuteQAbstractFormBuilderGadget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractFormBuilderGadget(
    QAbstractFormBuilderGadget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractFormBuilderGadget *>(self)->take(key, call);
}
