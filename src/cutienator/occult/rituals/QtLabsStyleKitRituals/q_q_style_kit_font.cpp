//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 19, as _ZNK14QQStyleKitFont6systemEv
inline QFont QQStyleKitFont::system() const { return m_fonts[int(QQuickTheme::System)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 20, as _ZNK14QQStyleKitFont6buttonEv
inline QFont QQStyleKitFont::button() const { return m_fonts[int(QQuickTheme::Button)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 21, as _ZNK14QQStyleKitFont8checkBoxEv
inline QFont QQStyleKitFont::checkBox() const { return m_fonts[int(QQuickTheme::CheckBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 22, as _ZNK14QQStyleKitFont8comboBoxEv
inline QFont QQStyleKitFont::comboBox() const { return m_fonts[int(QQuickTheme::ComboBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 23, as _ZNK14QQStyleKitFont8groupBoxEv
inline QFont QQStyleKitFont::groupBox() const { return m_fonts[int(QQuickTheme::GroupBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 24, as _ZNK14QQStyleKitFont12itemDelegateEv
inline QFont QQStyleKitFont::itemDelegate() const { return m_fonts[int(QQuickTheme::ItemView)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 25, as _ZNK14QQStyleKitFont5labelEv
inline QFont QQStyleKitFont::label() const { return m_fonts[int(QQuickTheme::Label)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 26, as _ZNK14QQStyleKitFont11radioButtonEv
inline QFont QQStyleKitFont::radioButton() const { return m_fonts[int(QQuickTheme::RadioButton)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 27, as _ZNK14QQStyleKitFont7spinBoxEv
inline QFont QQStyleKitFont::spinBox() const { return m_fonts[int(QQuickTheme::SpinBox)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 28, as _ZNK14QQStyleKitFont13switchControlEv
inline QFont QQStyleKitFont::switchControl() const { return m_fonts[int(QQuickTheme::Switch)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 29, as _ZNK14QQStyleKitFont6tabBarEv
inline QFont QQStyleKitFont::tabBar() const { return m_fonts[int(QQuickTheme::TabBar)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 30, as _ZNK14QQStyleKitFont8textAreaEv
inline QFont QQStyleKitFont::textArea() const { return m_fonts[int(QQuickTheme::TextArea)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 31, as _ZNK14QQStyleKitFont9textFieldEv
inline QFont QQStyleKitFont::textField() const { return m_fonts[int(QQuickTheme::TextField)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 32, as _ZNK14QQStyleKitFont7toolBarEv
inline QFont QQStyleKitFont::toolBar() const { return m_fonts[int(QQuickTheme::ToolBar)]; }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 69, as _ZNK14QQStyleKitFont12fallbackFontEv
inline QQStyleKitFont *QQStyleKitFont::fallbackFont() const
{
    return m_fallback;
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

//  QFont QQStyleKitFont::system() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont6systemEv(const QQStyleKitFont *self) {
  return new QFont(self->system());
}

//  QFont QQStyleKitFont::button() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont6buttonEv(const QQStyleKitFont *self) {
  return new QFont(self->button());
}

//  QFont QQStyleKitFont::checkBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8checkBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->checkBox());
}

//  QFont QQStyleKitFont::comboBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8comboBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->comboBox());
}

//  QFont QQStyleKitFont::groupBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8groupBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->groupBox());
}

//  QFont QQStyleKitFont::itemDelegate() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont12itemDelegateEv(
    const QQStyleKitFont *self) {
  return new QFont(self->itemDelegate());
}

//  QFont QQStyleKitFont::label() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont5labelEv(const QQStyleKitFont *self) {
  return new QFont(self->label());
}

//  QFont QQStyleKitFont::radioButton() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont11radioButtonEv(
    const QQStyleKitFont *self) {
  return new QFont(self->radioButton());
}

//  QFont QQStyleKitFont::spinBox() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont7spinBoxEv(const QQStyleKitFont *self) {
  return new QFont(self->spinBox());
}

//  QFont QQStyleKitFont::switchControl() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont13switchControlEv(
    const QQStyleKitFont *self) {
  return new QFont(self->switchControl());
}

//  QFont QQStyleKitFont::tabBar() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont6tabBarEv(const QQStyleKitFont *self) {
  return new QFont(self->tabBar());
}

//  QFont QQStyleKitFont::textArea() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont8textAreaEv(const QQStyleKitFont *self) {
  return new QFont(self->textArea());
}

//  QFont QQStyleKitFont::textField() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont9textFieldEv(const QQStyleKitFont *self) {
  return new QFont(self->textField());
}

//  QFont QQStyleKitFont::toolBar() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont7toolBarEv(const QQStyleKitFont *self) {
  return new QFont(self->toolBar());
}

//  QQStyleKitFont *QQStyleKitFont::fallbackFont() const
extern "C" Q_DECL_EXPORT
QQStyleKitFont *ritual_ZNK14QQStyleKitFont12fallbackFontEv(
    const QQStyleKitFont *self) {
  return self->fallbackFont();
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
