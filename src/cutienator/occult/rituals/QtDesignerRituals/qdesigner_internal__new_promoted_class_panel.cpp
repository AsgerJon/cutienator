//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_promotiondialog_p.h>
#include <QtDesigner/private/promotionmodel_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/private/signalslotdialog_p.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractpromotioninterface.h>
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtDesigner/abstractintegration.h>
#include <QtDesigner/private/abstractdialoggui_p.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtWidgets/qtreeview.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qcheckbox.h>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qlayoutitem.h>
#include <QtWidgets/qmenu.h>
#include <QtGui/qaction.h>
#include <QtGui/qvalidator.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qtimer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_promotiondialog.cpp, line 132, as _ZN18qdesigner_internal21NewPromotedClassPanel15slotNameChangedERK7QString
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void NewPromotedClassPanel::slotNameChanged(const QString &className) {
        // Suggest a name
        if (!className.isEmpty()) {
            QString suggestedHeader = m_promotedHeaderLowerCase ?
                                      className.toLower() : className;
            suggestedHeader.replace("::"_L1, "_"_L1);
            if (!m_promotedHeaderSuffix.startsWith(u'.'))
                suggestedHeader += u'.';
            suggestedHeader += m_promotedHeaderSuffix;

            const bool blocked = m_includeFileEdit->blockSignals(true);
            m_includeFileEdit->setText(suggestedHeader);
            m_includeFileEdit->blockSignals(blocked);
        }
        enableButtons();
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_promotiondialog.cpp, line 153, as _ZN18qdesigner_internal21NewPromotedClassPanel13enableButtonsEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void NewPromotedClassPanel::enableButtons() {
        const bool enabled = !m_classNameEdit->text().isEmpty() && !m_includeFileEdit->text().isEmpty();
        m_addButton->setEnabled(enabled);
        m_addButton->setDefault(enabled);
    }
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject
//      *qdesigner_internal::NewPromotedClassPanel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal21NewPromotedClassPanel10metaObjectEv(
    const qdesigner_internal::NewPromotedClassPanel *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::NewPromotedClassPanel::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal21NewPromotedClassPanel11qt_metacastEPKc(
    qdesigner_internal::NewPromotedClassPanel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      qdesigner_internal::NewPromotedClassPanel::qt_metacall(QMetaObject::C
//      all a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal21NewPromotedClassPanel11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::NewPromotedClassPanel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::NewPromotedClassPanel::promotedHeaderSuffix()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal21NewPromotedClassPanel20promotedHeaderSuffixEv(
    const qdesigner_internal::NewPromotedClassPanel *self) {
  return new QString(self->promotedHeaderSuffix());
}

//  void
//      qdesigner_internal::NewPromotedClassPanel::setPromotedHeaderSuffix(co
//      nst QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel23setPromotedHeaderSuffixERK7QString(
    qdesigner_internal::NewPromotedClassPanel *self,
    const QString *s) {
  self->setPromotedHeaderSuffix(*s);
}

//  bool
//      qdesigner_internal::NewPromotedClassPanel::isPromotedHeaderLowerCase(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal21NewPromotedClassPanel25isPromotedHeaderLowerCaseEv(
    const qdesigner_internal::NewPromotedClassPanel *self) {
  return self->isPromotedHeaderLowerCase();
}

//  void qdesigner_internal::NewPromotedClassPanel::setPromotedHeaderLowerCas
//      e(bool l)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel26setPromotedHeaderLowerCaseEb(
    qdesigner_internal::NewPromotedClassPanel *self,
    bool l) {
  self->setPromotedHeaderLowerCase(l);
}

//  void qdesigner_internal::NewPromotedClassPanel::grabFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel9grabFocusEv(
    qdesigner_internal::NewPromotedClassPanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::NewPromotedClassPanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "grabFocus()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "grabFocus()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::NewPromotedClassPanel::chooseBaseClass(const
//      QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel15chooseBaseClassERK7QString(
    qdesigner_internal::NewPromotedClassPanel *self,
    const QString *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::NewPromotedClassPanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "chooseBaseClass(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "chooseBaseClass(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::NewPromotedClassPanel::slotNameChanged(const
//      QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel15slotNameChangedERK7QString(
    qdesigner_internal::NewPromotedClassPanel *self,
    const QString *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::NewPromotedClassPanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotNameChanged(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotNameChanged(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      qdesigner_internal::NewPromotedClassPanel::slotIncludeFileChanged(con
//      st QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel22slotIncludeFileChangedERK7QString(
    qdesigner_internal::NewPromotedClassPanel *self,
    const QString *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::NewPromotedClassPanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotIncludeFileChanged(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotIncludeFileChanged(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::NewPromotedClassPanel::slotAdd()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel7slotAddEv(
    qdesigner_internal::NewPromotedClassPanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::NewPromotedClassPanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotAdd()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotAdd()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::NewPromotedClassPanel::slotReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel9slotResetEv(
    qdesigner_internal::NewPromotedClassPanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::NewPromotedClassPanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotReset()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotReset()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::NewPromotedClassPanel::enableButtons()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel13enableButtonsEv(
    qdesigner_internal::NewPromotedClassPanel *self) {
  self->enableButtons();
}
