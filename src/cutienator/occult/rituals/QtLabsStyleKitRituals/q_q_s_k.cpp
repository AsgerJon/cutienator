//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQSK' is pasted in, cut
//  from what the moc of Qt 6.12.0 writes for its header: Qt's library keeps
//  it to itself; added are 1 rituals that lean on what moc writes for a
//  class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#include <QtCore/qstring.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKit__QQSK.cpp, line 1, as moc:QQSK
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN4QQSKE_t {};
} // unnamed namespace

template <> constexpr inline auto QQSK::qt_create_metaobjectdata<qt_meta_tag_ZN4QQSKE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQSK",
        "Delegate",
        "NoDelegate",
        "Control",
        "Background",
        "Handle",
        "HandleFirst",
        "HandleSecond",
        "Indicator",
        "IndicatorForeground",
        "IndicatorFirst",
        "IndicatorFirstForeground",
        "IndicatorSecond",
        "IndicatorSecondForeground",
        "PropertyGroup",
        "Foreground",
        "Border",
        "Image",
        "Shadow",
        "Text",
        "PATH_ID_GROUP_COUNT",
        "DelegateSubtype0",
        "DelegateSubtype1",
        "DelegateSubtype2",
        "GlobalFlag",
        "Unspecified",
        "PropertyPathFlag",
        "NoFlags",
        "Global",
        "Property",
        "NoProperty",
        "BottomLeftRadius",
        "BottomMargin",
        "BottomPadding",
        "BottomRightRadius",
        "Clip",
        "Color",
        "Data",
        "FillMode",
        "FillWidth",
        "FillHeight",
        "Gradient",
        "HOffset",
        "LeftMargin",
        "LeftPadding",
        "Margins",
        "MinimumWidth",
        "MinimumHeight",
        "Opacity",
        "Padding",
        "Radius",
        "RightMargin",
        "RightPadding",
        "Rotation",
        "Scale",
        "Source",
        "Spacing",
        "TopLeftRadius",
        "TopMargin",
        "TopPadding",
        "TopRightRadius",
        "Transition",
        "Variations",
        "Visible",
        "VOffset",
        "Width",
        "Height",
        "Blur",
        "Alignment",
        "Bold",
        "Italic",
        "PointSize",
        "COUNT",
        "State",
        "StateFlag",
        "Normal",
        "Pressed",
        "Hovered",
        "Highlighted",
        "Focused",
        "Checked",
        "Vertical",
        "Disabled",
        "MAX_STATE",
        "Subclass",
        "QQStyleKitState",
        "QQStyleKitReader"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'Delegate'
        QtMocHelpers::EnumData<enum Delegate>(1, 1, QMC::EnumIsScoped).add({
            {    2, Delegate::NoDelegate },
            {    3, Delegate::Control },
            {    4, Delegate::Background },
            {    5, Delegate::Handle },
            {    6, Delegate::HandleFirst },
            {    7, Delegate::HandleSecond },
            {    8, Delegate::Indicator },
            {    9, Delegate::IndicatorForeground },
            {   10, Delegate::IndicatorFirst },
            {   11, Delegate::IndicatorFirstForeground },
            {   12, Delegate::IndicatorSecond },
            {   13, Delegate::IndicatorSecondForeground },
        }),
        // enum 'PropertyGroup'
        QtMocHelpers::EnumData<enum PropertyGroup>(14, 14, QMC::EnumIsScoped).add({
            {    3, PropertyGroup::Control },
            {    4, PropertyGroup::Background },
            {   15, PropertyGroup::Foreground },
            {   16, PropertyGroup::Border },
            {    5, PropertyGroup::Handle },
            {   17, PropertyGroup::Image },
            {    8, PropertyGroup::Indicator },
            {   18, PropertyGroup::Shadow },
            {   19, PropertyGroup::Text },
            {   20, PropertyGroup::PATH_ID_GROUP_COUNT },
            {   21, PropertyGroup::DelegateSubtype0 },
            {   22, PropertyGroup::DelegateSubtype1 },
            {   23, PropertyGroup::DelegateSubtype2 },
            {   24, PropertyGroup::GlobalFlag },
            {   25, PropertyGroup::Unspecified },
        }),
        // enum 'PropertyPathFlag'
        QtMocHelpers::EnumData<enum PropertyPathFlag>(26, 26, QMC::EnumIsScoped).add({
            {   27, PropertyPathFlag::NoFlags },
            {   21, PropertyPathFlag::DelegateSubtype0 },
            {   22, PropertyPathFlag::DelegateSubtype1 },
            {   23, PropertyPathFlag::DelegateSubtype2 },
            {   28, PropertyPathFlag::Global },
        }),
        // enum 'Property'
        QtMocHelpers::EnumData<enum Property>(29, 29, QMC::EnumIsScoped).add({
            {   30, Property::NoProperty },
            {   31, Property::BottomLeftRadius },
            {   32, Property::BottomMargin },
            {   33, Property::BottomPadding },
            {   34, Property::BottomRightRadius },
            {   35, Property::Clip },
            {   36, Property::Color },
            {   37, Property::Data },
            {    1, Property::Delegate },
            {   38, Property::FillMode },
            {   39, Property::FillWidth },
            {   40, Property::FillHeight },
            {   41, Property::Gradient },
            {   42, Property::HOffset },
            {   17, Property::Image },
            {   43, Property::LeftMargin },
            {   44, Property::LeftPadding },
            {   45, Property::Margins },
            {   46, Property::MinimumWidth },
            {   47, Property::MinimumHeight },
            {   48, Property::Opacity },
            {   49, Property::Padding },
            {   50, Property::Radius },
            {   51, Property::RightMargin },
            {   52, Property::RightPadding },
            {   53, Property::Rotation },
            {   54, Property::Scale },
            {   55, Property::Source },
            {   56, Property::Spacing },
            {   57, Property::TopLeftRadius },
            {   58, Property::TopMargin },
            {   59, Property::TopPadding },
            {   60, Property::TopRightRadius },
            {   61, Property::Transition },
            {   62, Property::Variations },
            {   63, Property::Visible },
            {   64, Property::VOffset },
            {   65, Property::Width },
            {   66, Property::Height },
            {   67, Property::Blur },
            {   68, Property::Alignment },
            {   69, Property::Bold },
            {   70, Property::Italic },
            {   71, Property::PointSize },
            {   72, Property::COUNT },
        }),
        // flag 'State'
        QtMocHelpers::EnumData<State>(73, 74, QMC::EnumIsFlag | QMC::EnumIsScoped).add({
            {   25, StateFlag::Unspecified },
            {   75, StateFlag::Normal },
            {   76, StateFlag::Pressed },
            {   77, StateFlag::Hovered },
            {   78, StateFlag::Highlighted },
            {   79, StateFlag::Focused },
            {   80, StateFlag::Checked },
            {   81, StateFlag::Vertical },
            {   82, StateFlag::Disabled },
            {   83, StateFlag::MAX_STATE },
        }),
        // enum 'Subclass'
        QtMocHelpers::EnumData<enum Subclass>(84, 84, QMC::EnumIsScoped).add({
            {   85, Subclass::QQStyleKitState },
            {   86, Subclass::QQStyleKitReader },
        }),
    };
    return QtMocHelpers::metaObjectData<QQSK, qt_meta_tag_ZN4QQSKE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQSK::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN4QQSKE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN4QQSKE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN4QQSKE_t>.metaTypes,
    nullptr
} };

void QQSK::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQSK *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQSK::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQSK::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN4QQSKE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQSK::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  A QQSK that Python can take functions over in. Every QQSK
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQSKCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQSKCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQSKCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQSKCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQSKCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQSKCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQSKCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQSK : public QQSK {
public:
  using QQSK::QQSK;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQSKCall0 call = reinterpret_cast<CuteQQSKCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQSKCall1 call = reinterpret_cast<CuteQQSKCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQSKCall2 call = reinterpret_cast<CuteQQSKCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQSKCall3 call = reinterpret_cast<CuteQQSKCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQSKCall4 call = reinterpret_cast<CuteQQSKCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQSKCall5 call = reinterpret_cast<CuteQQSKCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQSKCall6 call = reinterpret_cast<CuteQQSKCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQSK::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK4QQSK10metaObjectEv(const QQSK *self) {
  return self->metaObject();
}

//  void *QQSK::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN4QQSK11qt_metacastEPKc(QQSK *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQSK::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN4QQSK11qt_metacallEN11QMetaObject4CallEiPPv(
    QQSK *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQSK::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QQSK2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QQSK::tr(s, c, n));
}

//  a Python function taken by a CuteQQSK, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQSK(QQSK *self, const char *key, void *call) {
  return static_cast<CuteQQSK *>(self)->take(key, call);
}
