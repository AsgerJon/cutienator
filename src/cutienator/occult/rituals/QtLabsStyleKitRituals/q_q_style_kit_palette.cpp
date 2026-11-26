//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQStyleKitPalette' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 17 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsStyleKit/private/qqstylekitpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKit__QQStyleKitPalette.cpp, line 1, as moc:QQStyleKitPalette
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN17QQStyleKitPaletteE_t {};
} // unnamed namespace

template <> constexpr inline auto QQStyleKitPalette::qt_create_metaobjectdata<qt_meta_tag_ZN17QQStyleKitPaletteE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQStyleKitPalette",
        "QML.Element",
        "StylePalette",
        "systemChanged",
        "",
        "checkBoxChanged",
        "buttonChanged",
        "comboBoxChanged",
        "groupBoxChanged",
        "itemDelegateChanged",
        "labelChanged",
        "radioButtonChanged",
        "spinBoxChanged",
        "switchControlChanged",
        "tabBarChanged",
        "textAreaChanged",
        "textFieldChanged",
        "toolBarChanged",
        "fallbackPaletteChanged",
        "system",
        "QQuickPalette*",
        "checkBox",
        "button",
        "comboBox",
        "groupBox",
        "itemDelegate",
        "label",
        "radioButton",
        "spinBox",
        "switchControl",
        "tabBar",
        "textArea",
        "textField",
        "toolBar"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'systemChanged'
        QtMocHelpers::SignalData<void()>(3, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'checkBoxChanged'
        QtMocHelpers::SignalData<void()>(5, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'buttonChanged'
        QtMocHelpers::SignalData<void()>(6, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'comboBoxChanged'
        QtMocHelpers::SignalData<void()>(7, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'groupBoxChanged'
        QtMocHelpers::SignalData<void()>(8, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'itemDelegateChanged'
        QtMocHelpers::SignalData<void()>(9, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'labelChanged'
        QtMocHelpers::SignalData<void()>(10, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'radioButtonChanged'
        QtMocHelpers::SignalData<void()>(11, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'spinBoxChanged'
        QtMocHelpers::SignalData<void()>(12, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'switchControlChanged'
        QtMocHelpers::SignalData<void()>(13, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'tabBarChanged'
        QtMocHelpers::SignalData<void()>(14, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'textAreaChanged'
        QtMocHelpers::SignalData<void()>(15, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'textFieldChanged'
        QtMocHelpers::SignalData<void()>(16, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'toolBarChanged'
        QtMocHelpers::SignalData<void()>(17, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'fallbackPaletteChanged'
        QtMocHelpers::SignalData<void()>(18, 4, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'system'
        QtMocHelpers::PropertyData<QQuickPalette*>(19, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'checkBox'
        QtMocHelpers::PropertyData<QQuickPalette*>(21, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 1),
        // property 'button'
        QtMocHelpers::PropertyData<QQuickPalette*>(22, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 2),
        // property 'comboBox'
        QtMocHelpers::PropertyData<QQuickPalette*>(23, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 3),
        // property 'groupBox'
        QtMocHelpers::PropertyData<QQuickPalette*>(24, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 4),
        // property 'itemDelegate'
        QtMocHelpers::PropertyData<QQuickPalette*>(25, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 5),
        // property 'label'
        QtMocHelpers::PropertyData<QQuickPalette*>(26, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 6),
        // property 'radioButton'
        QtMocHelpers::PropertyData<QQuickPalette*>(27, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 7),
        // property 'spinBox'
        QtMocHelpers::PropertyData<QQuickPalette*>(28, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 8),
        // property 'switchControl'
        QtMocHelpers::PropertyData<QQuickPalette*>(29, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 9),
        // property 'tabBar'
        QtMocHelpers::PropertyData<QQuickPalette*>(30, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 10),
        // property 'textArea'
        QtMocHelpers::PropertyData<QQuickPalette*>(31, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 11),
        // property 'textField'
        QtMocHelpers::PropertyData<QQuickPalette*>(32, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 12),
        // property 'toolBar'
        QtMocHelpers::PropertyData<QQuickPalette*>(33, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 13),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQStyleKitPalette, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQStyleKitPalette::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QQStyleKitPaletteE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QQStyleKitPaletteE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN17QQStyleKitPaletteE_t>.metaTypes,
    nullptr
} };

void QQStyleKitPalette::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQStyleKitPalette *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->systemChanged(); break;
        case 1: _t->checkBoxChanged(); break;
        case 2: _t->buttonChanged(); break;
        case 3: _t->comboBoxChanged(); break;
        case 4: _t->groupBoxChanged(); break;
        case 5: _t->itemDelegateChanged(); break;
        case 6: _t->labelChanged(); break;
        case 7: _t->radioButtonChanged(); break;
        case 8: _t->spinBoxChanged(); break;
        case 9: _t->switchControlChanged(); break;
        case 10: _t->tabBarChanged(); break;
        case 11: _t->textAreaChanged(); break;
        case 12: _t->textFieldChanged(); break;
        case 13: _t->toolBarChanged(); break;
        case 14: _t->fallbackPaletteChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::systemChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::checkBoxChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::buttonChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::comboBoxChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::groupBoxChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::itemDelegateChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::labelChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::radioButtonChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::spinBoxChanged, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::switchControlChanged, 9))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::tabBarChanged, 10))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::textAreaChanged, 11))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::textFieldChanged, 12))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::toolBarChanged, 13))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitPalette::*)()>(_a, &QQStyleKitPalette::fallbackPaletteChanged, 14))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 13:
        case 12:
        case 11:
        case 10:
        case 9:
        case 8:
        case 7:
        case 6:
        case 5:
        case 4:
        case 3:
        case 2:
        case 1:
        case 0:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QQuickPalette* >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQuickPalette**>(_v) = _t->system(); break;
        case 1: *reinterpret_cast<QQuickPalette**>(_v) = _t->checkBox(); break;
        case 2: *reinterpret_cast<QQuickPalette**>(_v) = _t->button(); break;
        case 3: *reinterpret_cast<QQuickPalette**>(_v) = _t->comboBox(); break;
        case 4: *reinterpret_cast<QQuickPalette**>(_v) = _t->groupBox(); break;
        case 5: *reinterpret_cast<QQuickPalette**>(_v) = _t->itemDelegate(); break;
        case 6: *reinterpret_cast<QQuickPalette**>(_v) = _t->label(); break;
        case 7: *reinterpret_cast<QQuickPalette**>(_v) = _t->radioButton(); break;
        case 8: *reinterpret_cast<QQuickPalette**>(_v) = _t->spinBox(); break;
        case 9: *reinterpret_cast<QQuickPalette**>(_v) = _t->switchControl(); break;
        case 10: *reinterpret_cast<QQuickPalette**>(_v) = _t->tabBar(); break;
        case 11: *reinterpret_cast<QQuickPalette**>(_v) = _t->textArea(); break;
        case 12: *reinterpret_cast<QQuickPalette**>(_v) = _t->textField(); break;
        case 13: *reinterpret_cast<QQuickPalette**>(_v) = _t->toolBar(); break;
        default: break;
        }
    }
}

const QMetaObject *QQStyleKitPalette::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQStyleKitPalette::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QQStyleKitPaletteE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQStyleKitPalette::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 15)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 15;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 15)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 15;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 14;
    }
    return _id;
}

// SIGNAL 0
void QQStyleKitPalette::systemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQStyleKitPalette::checkBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQStyleKitPalette::buttonChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQStyleKitPalette::comboBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQStyleKitPalette::groupBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void QQStyleKitPalette::itemDelegateChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void QQStyleKitPalette::labelChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void QQStyleKitPalette::radioButtonChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void QQStyleKitPalette::spinBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}

// SIGNAL 9
void QQStyleKitPalette::switchControlChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 9, nullptr);
}

// SIGNAL 10
void QQStyleKitPalette::tabBarChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 10, nullptr);
}

// SIGNAL 11
void QQStyleKitPalette::textAreaChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 11, nullptr);
}

// SIGNAL 12
void QQStyleKitPalette::textFieldChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 12, nullptr);
}

// SIGNAL 13
void QQStyleKitPalette::toolBarChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 13, nullptr);
}

// SIGNAL 14
void QQStyleKitPalette::fallbackPaletteChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 14, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 8, as _ZN17QQStyleKitPaletteC1EP7QObject
inline QQStyleKitPalette::QQStyleKitPalette(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 28, as _ZNK17QQStyleKitPalette6systemEv
inline QQuickPalette *QQStyleKitPalette::system() const { if (!m_system) { m_system.reset(new QQuickPalette()); QObject::connect(m_system.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::System); emit self->systemChanged(); }); } return m_system.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 29, as _ZNK17QQStyleKitPalette8checkBoxEv
inline QQuickPalette *QQStyleKitPalette::checkBox() const { if (!m_checkBox) { m_checkBox.reset(new QQuickPalette()); QObject::connect(m_checkBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::CheckBox); emit self->checkBoxChanged(); }); } return m_checkBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 30, as _ZNK17QQStyleKitPalette6buttonEv
inline QQuickPalette *QQStyleKitPalette::button() const { if (!m_button) { m_button.reset(new QQuickPalette()); QObject::connect(m_button.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::Button); emit self->buttonChanged(); }); } return m_button.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 31, as _ZNK17QQStyleKitPalette8comboBoxEv
inline QQuickPalette *QQStyleKitPalette::comboBox() const { if (!m_comboBox) { m_comboBox.reset(new QQuickPalette()); QObject::connect(m_comboBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::ComboBox); emit self->comboBoxChanged(); }); } return m_comboBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 32, as _ZNK17QQStyleKitPalette8groupBoxEv
inline QQuickPalette *QQStyleKitPalette::groupBox() const { if (!m_groupBox) { m_groupBox.reset(new QQuickPalette()); QObject::connect(m_groupBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::GroupBox); emit self->groupBoxChanged(); }); } return m_groupBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 33, as _ZNK17QQStyleKitPalette12itemDelegateEv
inline QQuickPalette *QQStyleKitPalette::itemDelegate() const { if (!m_itemDelegate) { m_itemDelegate.reset(new QQuickPalette()); QObject::connect(m_itemDelegate.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::ItemView); emit self->itemDelegateChanged(); }); } return m_itemDelegate.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 34, as _ZNK17QQStyleKitPalette5labelEv
inline QQuickPalette *QQStyleKitPalette::label() const { if (!m_label) { m_label.reset(new QQuickPalette()); QObject::connect(m_label.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::Label); emit self->labelChanged(); }); } return m_label.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 35, as _ZNK17QQStyleKitPalette11radioButtonEv
inline QQuickPalette *QQStyleKitPalette::radioButton() const { if (!m_radioButton) { m_radioButton.reset(new QQuickPalette()); QObject::connect(m_radioButton.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::RadioButton); emit self->radioButtonChanged(); }); } return m_radioButton.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 36, as _ZNK17QQStyleKitPalette7spinBoxEv
inline QQuickPalette *QQStyleKitPalette::spinBox() const { if (!m_spinBox) { m_spinBox.reset(new QQuickPalette()); QObject::connect(m_spinBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::SpinBox); emit self->spinBoxChanged(); }); } return m_spinBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 37, as _ZNK17QQStyleKitPalette13switchControlEv
inline QQuickPalette *QQStyleKitPalette::switchControl() const { if (!m_switchControl) { m_switchControl.reset(new QQuickPalette()); QObject::connect(m_switchControl.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::Switch); emit self->switchControlChanged(); }); } return m_switchControl.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 38, as _ZNK17QQStyleKitPalette6tabBarEv
inline QQuickPalette *QQStyleKitPalette::tabBar() const { if (!m_tabBar) { m_tabBar.reset(new QQuickPalette()); QObject::connect(m_tabBar.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::TabBar); emit self->tabBarChanged(); }); } return m_tabBar.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 39, as _ZNK17QQStyleKitPalette8textAreaEv
inline QQuickPalette *QQStyleKitPalette::textArea() const { if (!m_textArea) { m_textArea.reset(new QQuickPalette()); QObject::connect(m_textArea.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::TextArea); emit self->textAreaChanged(); }); } return m_textArea.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 40, as _ZNK17QQStyleKitPalette9textFieldEv
inline QQuickPalette *QQStyleKitPalette::textField() const { if (!m_textField) { m_textField.reset(new QQuickPalette()); QObject::connect(m_textField.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::TextField); emit self->textFieldChanged(); }); } return m_textField.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 41, as _ZNK17QQStyleKitPalette7toolBarEv
inline QQuickPalette *QQStyleKitPalette::toolBar() const { if (!m_toolBar) { m_toolBar.reset(new QQuickPalette()); QObject::connect(m_toolBar.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::ToolBar); emit self->toolBarChanged(); }); } return m_toolBar.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 43, as _ZNK17QQStyleKitPalette15fallbackPaletteEv
inline QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
{
    return m_fallbackPalette;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 48, as _ZN17QQStyleKitPalette18setFallbackPaletteEPS_
inline void QQStyleKitPalette::setFallbackPalette(QQStyleKitPalette *palette)
{
    if (m_fallbackPalette == palette)
        return;

    m_fallbackPalette = palette;
    emit fallbackPaletteChanged();
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

//  QString QQStyleKitPalette::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQStyleKitPalette2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitPalette::tr(s, c, n));
}

//  QQStyleKitPalette::QQStyleKitPalette(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitPalette *ritual_ZN17QQStyleKitPaletteC1EP7QObject(
    QObject *parent) {
  return new QQStyleKitPalette(parent);
}

//  QQuickPalette *QQStyleKitPalette::system() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette6systemEv(
    const QQStyleKitPalette *self) {
  return self->system();
}

//  QQuickPalette *QQStyleKitPalette::checkBox() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette8checkBoxEv(
    const QQStyleKitPalette *self) {
  return self->checkBox();
}

//  QQuickPalette *QQStyleKitPalette::button() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette6buttonEv(
    const QQStyleKitPalette *self) {
  return self->button();
}

//  QQuickPalette *QQStyleKitPalette::comboBox() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette8comboBoxEv(
    const QQStyleKitPalette *self) {
  return self->comboBox();
}

//  QQuickPalette *QQStyleKitPalette::groupBox() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette8groupBoxEv(
    const QQStyleKitPalette *self) {
  return self->groupBox();
}

//  QQuickPalette *QQStyleKitPalette::itemDelegate() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette12itemDelegateEv(
    const QQStyleKitPalette *self) {
  return self->itemDelegate();
}

//  QQuickPalette *QQStyleKitPalette::label() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette5labelEv(
    const QQStyleKitPalette *self) {
  return self->label();
}

//  QQuickPalette *QQStyleKitPalette::radioButton() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette11radioButtonEv(
    const QQStyleKitPalette *self) {
  return self->radioButton();
}

//  QQuickPalette *QQStyleKitPalette::spinBox() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette7spinBoxEv(
    const QQStyleKitPalette *self) {
  return self->spinBox();
}

//  QQuickPalette *QQStyleKitPalette::switchControl() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette13switchControlEv(
    const QQStyleKitPalette *self) {
  return self->switchControl();
}

//  QQuickPalette *QQStyleKitPalette::tabBar() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette6tabBarEv(
    const QQStyleKitPalette *self) {
  return self->tabBar();
}

//  QQuickPalette *QQStyleKitPalette::textArea() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette8textAreaEv(
    const QQStyleKitPalette *self) {
  return self->textArea();
}

//  QQuickPalette *QQStyleKitPalette::textField() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette9textFieldEv(
    const QQStyleKitPalette *self) {
  return self->textField();
}

//  QQuickPalette *QQStyleKitPalette::toolBar() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK17QQStyleKitPalette7toolBarEv(
    const QQStyleKitPalette *self) {
  return self->toolBar();
}

//  QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
extern "C" Q_DECL_EXPORT
QQStyleKitPalette *ritual_ZNK17QQStyleKitPalette15fallbackPaletteEv(
    const QQStyleKitPalette *self) {
  return self->fallbackPalette();
}

//  void QQStyleKitPalette::setFallbackPalette(QQStyleKitPalette *fallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette18setFallbackPaletteEPS_(
    QQStyleKitPalette *self,
    QQStyleKitPalette *fallback) {
  self->setFallbackPalette(fallback);
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
