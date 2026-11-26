//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQStyleKitFont' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 17 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsStyleKit/private/qqstylekitfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKit__QQStyleKitFont.cpp, line 1, as moc:QQStyleKitFont
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN14QQStyleKitFontE_t {};
} // unnamed namespace

template <> constexpr inline auto QQStyleKitFont::qt_create_metaobjectdata<qt_meta_tag_ZN14QQStyleKitFontE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQStyleKitFont",
        "QML.Element",
        "StyleFont",
        "systemChanged",
        "",
        "buttonChanged",
        "checkBoxChanged",
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
        "fallbackFontChanged",
        "system",
        "QFont",
        "button",
        "checkBox",
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
        // Signal 'buttonChanged'
        QtMocHelpers::SignalData<void()>(5, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'checkBoxChanged'
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
        // Signal 'fallbackFontChanged'
        QtMocHelpers::SignalData<void()>(18, 4, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'system'
        QtMocHelpers::PropertyData<QFont>(19, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 0),
        // property 'button'
        QtMocHelpers::PropertyData<QFont>(21, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 1),
        // property 'checkBox'
        QtMocHelpers::PropertyData<QFont>(22, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 2),
        // property 'comboBox'
        QtMocHelpers::PropertyData<QFont>(23, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 3),
        // property 'groupBox'
        QtMocHelpers::PropertyData<QFont>(24, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 4),
        // property 'itemDelegate'
        QtMocHelpers::PropertyData<QFont>(25, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 5),
        // property 'label'
        QtMocHelpers::PropertyData<QFont>(26, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 6),
        // property 'radioButton'
        QtMocHelpers::PropertyData<QFont>(27, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 7),
        // property 'spinBox'
        QtMocHelpers::PropertyData<QFont>(28, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 8),
        // property 'switchControl'
        QtMocHelpers::PropertyData<QFont>(29, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 9),
        // property 'tabBar'
        QtMocHelpers::PropertyData<QFont>(30, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 10),
        // property 'textArea'
        QtMocHelpers::PropertyData<QFont>(31, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 11),
        // property 'textField'
        QtMocHelpers::PropertyData<QFont>(32, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 12),
        // property 'toolBar'
        QtMocHelpers::PropertyData<QFont>(33, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 13),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQStyleKitFont, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQStyleKitFont::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QQStyleKitFontE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QQStyleKitFontE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN14QQStyleKitFontE_t>.metaTypes,
    nullptr
} };

void QQStyleKitFont::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQStyleKitFont *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->systemChanged(); break;
        case 1: _t->buttonChanged(); break;
        case 2: _t->checkBoxChanged(); break;
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
        case 14: _t->fallbackFontChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::systemChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::buttonChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::checkBoxChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::comboBoxChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::groupBoxChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::itemDelegateChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::labelChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::radioButtonChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::spinBoxChanged, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::switchControlChanged, 9))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::tabBarChanged, 10))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::textAreaChanged, 11))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::textFieldChanged, 12))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::toolBarChanged, 13))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitFont::*)()>(_a, &QQStyleKitFont::fallbackFontChanged, 14))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QFont*>(_v) = _t->system(); break;
        case 1: *reinterpret_cast<QFont*>(_v) = _t->button(); break;
        case 2: *reinterpret_cast<QFont*>(_v) = _t->checkBox(); break;
        case 3: *reinterpret_cast<QFont*>(_v) = _t->comboBox(); break;
        case 4: *reinterpret_cast<QFont*>(_v) = _t->groupBox(); break;
        case 5: *reinterpret_cast<QFont*>(_v) = _t->itemDelegate(); break;
        case 6: *reinterpret_cast<QFont*>(_v) = _t->label(); break;
        case 7: *reinterpret_cast<QFont*>(_v) = _t->radioButton(); break;
        case 8: *reinterpret_cast<QFont*>(_v) = _t->spinBox(); break;
        case 9: *reinterpret_cast<QFont*>(_v) = _t->switchControl(); break;
        case 10: *reinterpret_cast<QFont*>(_v) = _t->tabBar(); break;
        case 11: *reinterpret_cast<QFont*>(_v) = _t->textArea(); break;
        case 12: *reinterpret_cast<QFont*>(_v) = _t->textField(); break;
        case 13: *reinterpret_cast<QFont*>(_v) = _t->toolBar(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setSystem(*reinterpret_cast<QFont*>(_v)); break;
        case 1: _t->setButton(*reinterpret_cast<QFont*>(_v)); break;
        case 2: _t->setCheckBox(*reinterpret_cast<QFont*>(_v)); break;
        case 3: _t->setComboBox(*reinterpret_cast<QFont*>(_v)); break;
        case 4: _t->setGroupBox(*reinterpret_cast<QFont*>(_v)); break;
        case 5: _t->setItemDelegate(*reinterpret_cast<QFont*>(_v)); break;
        case 6: _t->setLabel(*reinterpret_cast<QFont*>(_v)); break;
        case 7: _t->setRadioButton(*reinterpret_cast<QFont*>(_v)); break;
        case 8: _t->setSpinBox(*reinterpret_cast<QFont*>(_v)); break;
        case 9: _t->setSwitchControl(*reinterpret_cast<QFont*>(_v)); break;
        case 10: _t->setTabBar(*reinterpret_cast<QFont*>(_v)); break;
        case 11: _t->setTextArea(*reinterpret_cast<QFont*>(_v)); break;
        case 12: _t->setTextField(*reinterpret_cast<QFont*>(_v)); break;
        case 13: _t->setToolBar(*reinterpret_cast<QFont*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQStyleKitFont::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQStyleKitFont::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QQStyleKitFontE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQStyleKitFont::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
void QQStyleKitFont::systemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQStyleKitFont::buttonChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQStyleKitFont::checkBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQStyleKitFont::comboBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQStyleKitFont::groupBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void QQStyleKitFont::itemDelegateChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void QQStyleKitFont::labelChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void QQStyleKitFont::radioButtonChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void QQStyleKitFont::spinBoxChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}

// SIGNAL 9
void QQStyleKitFont::switchControlChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 9, nullptr);
}

// SIGNAL 10
void QQStyleKitFont::tabBarChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 10, nullptr);
}

// SIGNAL 11
void QQStyleKitFont::textAreaChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 11, nullptr);
}

// SIGNAL 12
void QQStyleKitFont::textFieldChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 12, nullptr);
}

// SIGNAL 13
void QQStyleKitFont::toolBarChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 13, nullptr);
}

// SIGNAL 14
void QQStyleKitFont::fallbackFontChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 14, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 55, as _ZN14QQStyleKitFont15setFontForScopeEN11QQuickTheme5ScopeERK5QFontMS_FvvE
inline void QQStyleKitFont::setFontForScope(QQuickTheme::Scope scope, const QFont &font, void (QQStyleKitFont::*signal)())
{
    const int index = int(scope);
    if (isSet(scope) && m_fonts[index] == font)
        return;

    m_fonts[index] = font;
    markSet(scope);
    emit (this->*signal)();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 8, as _ZN14QQStyleKitFontC1EP7QObject
inline QQStyleKitFont::QQStyleKitFont(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 19, as _ZNK14QQStyleKitFont6systemEv
inline QFont QQStyleKitFont::system() const { return m_fonts[int(QQuickTheme::System)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 40, as _ZN14QQStyleKitFont9setSystemERK5QFont
inline void QQStyleKitFont::setSystem(const QFont &font) { setFontForScope(QQuickTheme::System, font, &QQStyleKitFont::systemChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 20, as _ZNK14QQStyleKitFont6buttonEv
inline QFont QQStyleKitFont::button() const { return m_fonts[int(QQuickTheme::Button)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 41, as _ZN14QQStyleKitFont9setButtonERK5QFont
inline void QQStyleKitFont::setButton(const QFont &font) { setFontForScope(QQuickTheme::Button, font, &QQStyleKitFont::buttonChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 21, as _ZNK14QQStyleKitFont8checkBoxEv
inline QFont QQStyleKitFont::checkBox() const { return m_fonts[int(QQuickTheme::CheckBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 42, as _ZN14QQStyleKitFont11setCheckBoxERK5QFont
inline void QQStyleKitFont::setCheckBox(const QFont &font) { setFontForScope(QQuickTheme::CheckBox, font, &QQStyleKitFont::checkBoxChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 22, as _ZNK14QQStyleKitFont8comboBoxEv
inline QFont QQStyleKitFont::comboBox() const { return m_fonts[int(QQuickTheme::ComboBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 43, as _ZN14QQStyleKitFont11setComboBoxERK5QFont
inline void QQStyleKitFont::setComboBox(const QFont &font) { setFontForScope(QQuickTheme::ComboBox, font, &QQStyleKitFont::comboBoxChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 23, as _ZNK14QQStyleKitFont8groupBoxEv
inline QFont QQStyleKitFont::groupBox() const { return m_fonts[int(QQuickTheme::GroupBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 44, as _ZN14QQStyleKitFont11setGroupBoxERK5QFont
inline void QQStyleKitFont::setGroupBox(const QFont &font) { setFontForScope(QQuickTheme::GroupBox, font, &QQStyleKitFont::groupBoxChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 24, as _ZNK14QQStyleKitFont12itemDelegateEv
inline QFont QQStyleKitFont::itemDelegate() const { return m_fonts[int(QQuickTheme::ItemView)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 45, as _ZN14QQStyleKitFont15setItemDelegateERK5QFont
inline void QQStyleKitFont::setItemDelegate(const QFont &font) { setFontForScope(QQuickTheme::ItemView, font, &QQStyleKitFont::itemDelegateChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 25, as _ZNK14QQStyleKitFont5labelEv
inline QFont QQStyleKitFont::label() const { return m_fonts[int(QQuickTheme::Label)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 46, as _ZN14QQStyleKitFont8setLabelERK5QFont
inline void QQStyleKitFont::setLabel(const QFont &font) { setFontForScope(QQuickTheme::Label, font, &QQStyleKitFont::labelChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 26, as _ZNK14QQStyleKitFont11radioButtonEv
inline QFont QQStyleKitFont::radioButton() const { return m_fonts[int(QQuickTheme::RadioButton)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 47, as _ZN14QQStyleKitFont14setRadioButtonERK5QFont
inline void QQStyleKitFont::setRadioButton(const QFont &font) { setFontForScope(QQuickTheme::RadioButton, font, &QQStyleKitFont::radioButtonChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 27, as _ZNK14QQStyleKitFont7spinBoxEv
inline QFont QQStyleKitFont::spinBox() const { return m_fonts[int(QQuickTheme::SpinBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 48, as _ZN14QQStyleKitFont10setSpinBoxERK5QFont
inline void QQStyleKitFont::setSpinBox(const QFont &font) { setFontForScope(QQuickTheme::SpinBox, font, &QQStyleKitFont::spinBoxChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 28, as _ZNK14QQStyleKitFont13switchControlEv
inline QFont QQStyleKitFont::switchControl() const { return m_fonts[int(QQuickTheme::Switch)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 49, as _ZN14QQStyleKitFont16setSwitchControlERK5QFont
inline void QQStyleKitFont::setSwitchControl(const QFont &font) { setFontForScope(QQuickTheme::Switch, font, &QQStyleKitFont::switchControlChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 29, as _ZNK14QQStyleKitFont6tabBarEv
inline QFont QQStyleKitFont::tabBar() const { return m_fonts[int(QQuickTheme::TabBar)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 50, as _ZN14QQStyleKitFont9setTabBarERK5QFont
inline void QQStyleKitFont::setTabBar(const QFont &font) { setFontForScope(QQuickTheme::TabBar, font, &QQStyleKitFont::tabBarChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 30, as _ZNK14QQStyleKitFont8textAreaEv
inline QFont QQStyleKitFont::textArea() const { return m_fonts[int(QQuickTheme::TextArea)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 51, as _ZN14QQStyleKitFont11setTextAreaERK5QFont
inline void QQStyleKitFont::setTextArea(const QFont &font) { setFontForScope(QQuickTheme::TextArea, font, &QQStyleKitFont::textAreaChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 31, as _ZNK14QQStyleKitFont9textFieldEv
inline QFont QQStyleKitFont::textField() const { return m_fonts[int(QQuickTheme::TextField)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 52, as _ZN14QQStyleKitFont12setTextFieldERK5QFont
inline void QQStyleKitFont::setTextField(const QFont &font) { setFontForScope(QQuickTheme::TextField, font, &QQStyleKitFont::textFieldChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 32, as _ZNK14QQStyleKitFont7toolBarEv
inline QFont QQStyleKitFont::toolBar() const { return m_fonts[int(QQuickTheme::ToolBar)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 53, as _ZN14QQStyleKitFont10setToolBarERK5QFont
inline void QQStyleKitFont::setToolBar(const QFont &font) { setFontForScope(QQuickTheme::ToolBar, font, &QQStyleKitFont::toolBarChanged); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 69, as _ZNK14QQStyleKitFont12fallbackFontEv
inline QQStyleKitFont *QQStyleKitFont::fallbackFont() const
{
    return m_fallback;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 74, as _ZN14QQStyleKitFont15setFallbackFontEPS_
inline void QQStyleKitFont::setFallbackFont(QQStyleKitFont *fallback)
{
    if (m_fallback == fallback)
        return;

    m_fallback = fallback;
    emit fallbackFontChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 83, as _ZNK14QQStyleKitFont12fontForScopeEN11QQuickTheme5ScopeE
inline QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope) const
{
    return m_fonts[int(scope)];
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitFont::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQStyleKitFont10metaObjectEv(
    const QQStyleKitFont *self) {
  return self->metaObject();
}

//  void *QQStyleKitFont::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQStyleKitFont11qt_metacastEPKc(
    QQStyleKitFont *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitFont::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQStyleKitFont11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitFont *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitFont::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQStyleKitFont2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitFont::tr(s, c, n));
}

//  QQStyleKitFont::QQStyleKitFont(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitFont *ritual_ZN14QQStyleKitFontC1EP7QObject(QObject *parent) {
  return new QQStyleKitFont(parent);
}

//  QFont QQStyleKitFont::system() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont6systemEv(const QQStyleKitFont *self) {
  return new QFont(self->system());
}

//  void QQStyleKitFont::setSystem(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont9setSystemERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setSystem(*font);
}

//  QFont QQStyleKitFont::button() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont6buttonEv(const QQStyleKitFont *self) {
  return new QFont(self->button());
}

//  void QQStyleKitFont::setButton(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont9setButtonERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setButton(*font);
}

//  QFont QQStyleKitFont::checkBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8checkBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->checkBox());
}

//  void QQStyleKitFont::setCheckBox(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont11setCheckBoxERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setCheckBox(*font);
}

//  QFont QQStyleKitFont::comboBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8comboBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->comboBox());
}

//  void QQStyleKitFont::setComboBox(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont11setComboBoxERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setComboBox(*font);
}

//  QFont QQStyleKitFont::groupBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8groupBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->groupBox());
}

//  void QQStyleKitFont::setGroupBox(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont11setGroupBoxERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setGroupBox(*font);
}

//  QFont QQStyleKitFont::itemDelegate() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont12itemDelegateEv(
    const QQStyleKitFont *self) {
  return new QFont(self->itemDelegate());
}

//  void QQStyleKitFont::setItemDelegate(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont15setItemDelegateERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setItemDelegate(*font);
}

//  QFont QQStyleKitFont::label() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont5labelEv(const QQStyleKitFont *self) {
  return new QFont(self->label());
}

//  void QQStyleKitFont::setLabel(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont8setLabelERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setLabel(*font);
}

//  QFont QQStyleKitFont::radioButton() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont11radioButtonEv(
    const QQStyleKitFont *self) {
  return new QFont(self->radioButton());
}

//  void QQStyleKitFont::setRadioButton(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont14setRadioButtonERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setRadioButton(*font);
}

//  QFont QQStyleKitFont::spinBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont7spinBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->spinBox());
}

//  void QQStyleKitFont::setSpinBox(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont10setSpinBoxERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setSpinBox(*font);
}

//  QFont QQStyleKitFont::switchControl() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont13switchControlEv(
    const QQStyleKitFont *self) {
  return new QFont(self->switchControl());
}

//  void QQStyleKitFont::setSwitchControl(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont16setSwitchControlERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setSwitchControl(*font);
}

//  QFont QQStyleKitFont::tabBar() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont6tabBarEv(const QQStyleKitFont *self) {
  return new QFont(self->tabBar());
}

//  void QQStyleKitFont::setTabBar(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont9setTabBarERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setTabBar(*font);
}

//  QFont QQStyleKitFont::textArea() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8textAreaEv(const QQStyleKitFont *self) {
  return new QFont(self->textArea());
}

//  void QQStyleKitFont::setTextArea(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont11setTextAreaERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setTextArea(*font);
}

//  QFont QQStyleKitFont::textField() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont9textFieldEv(const QQStyleKitFont *self) {
  return new QFont(self->textField());
}

//  void QQStyleKitFont::setTextField(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont12setTextFieldERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setTextField(*font);
}

//  QFont QQStyleKitFont::toolBar() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont7toolBarEv(const QQStyleKitFont *self) {
  return new QFont(self->toolBar());
}

//  void QQStyleKitFont::setToolBar(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont10setToolBarERK5QFont(
    QQStyleKitFont *self,
    const QFont *font) {
  self->setToolBar(*font);
}

//  QQStyleKitFont *QQStyleKitFont::fallbackFont() const
extern "C" Q_DECL_EXPORT
QQStyleKitFont *ritual_ZNK14QQStyleKitFont12fallbackFontEv(
    const QQStyleKitFont *self) {
  return self->fallbackFont();
}

//  void QQStyleKitFont::setFallbackFont(QQStyleKitFont *fallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont15setFallbackFontEPS_(
    QQStyleKitFont *self,
    QQStyleKitFont *fallback) {
  self->setFallbackFont(fallback);
}

//  void QQStyleKitFont::systemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont13systemChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::buttonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont13buttonChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::checkBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont15checkBoxChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::comboBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont15comboBoxChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::groupBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont15groupBoxChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::itemDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont19itemDelegateChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::labelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont12labelChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::radioButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont18radioButtonChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::spinBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont14spinBoxChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::switchControlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont20switchControlChangedEv(
    QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::tabBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont13tabBarChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::textAreaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont15textAreaChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::textFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont16textFieldChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::toolBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont14toolBarChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
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

//  void QQStyleKitFont::fallbackFontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont19fallbackFontChangedEv(QQStyleKitFont *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitFont")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fallbackFontChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fallbackFontChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont12fontForScopeEN11QQuickTheme5ScopeE(
    const QQStyleKitFont *self,
    QQuickTheme::Scope scope) {
  return new QFont(self->fontForScope(scope));
}

//  bool QQStyleKitFont::isSet(QQuickTheme::Scope scope) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQStyleKitFont5isSetEN11QQuickTheme5ScopeE(
    const QQStyleKitFont *self,
    QQuickTheme::Scope scope) {
  return self->isSet(scope);
}

//  void QQStyleKitFont::markSet(QQuickTheme::Scope scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont7markSetEN11QQuickTheme5ScopeE(
    QQStyleKitFont *self,
    QQuickTheme::Scope scope) {
  self->markSet(scope);
}
