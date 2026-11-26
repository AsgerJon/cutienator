//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/signalslotdialog_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/private/qdesigner_formwindowcommand_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/membersheet.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/private/abstractdialoggui_p.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qvalidator.h>
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qmessagebox.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 36, as local:signalslotdialog.cpp:signatureRegExp
static constexpr auto signatureRegExp = "^[\\w+_]+\\(([\\w+:]\\*?,?)*\\)$"_L1;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 37, as local:signalslotdialog.cpp:methodNameRegExp
static constexpr auto methodNameRegExp = "^[\\w+_]+$"_L1;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 39, as local:signalslotdialog.cpp:createEditableItem
static QStandardItem *createEditableItem(const QString &text)
{
    QStandardItem *rc = new QStandardItem(text);
    rc->setFlags(Qt::ItemIsEnabled|Qt::ItemIsEditable|Qt::ItemIsSelectable);
    return rc;
}

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 46, as local:signalslotdialog.cpp:createDisabledItem
static QStandardItem *createDisabledItem(const QString &text)
{
    QStandardItem *rc = new QStandardItem(text);
    Qt::ItemFlags flags = rc->flags();
    rc->setFlags(flags & ~(Qt::ItemIsEnabled|Qt::ItemIsEditable|Qt::ItemIsSelectable));
    return rc;
}

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 57, as local:signalslotdialog.cpp:SignatureDelegate
namespace {
class SignatureDelegate : public QStyledItemDelegate {
    public:
        SignatureDelegate(QObject * parent = nullptr);
        QWidget * createEditor (QWidget * parent, const QStyleOptionViewItem &option, const QModelIndex &index ) const override;
        void setModelData (QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const override;

    private:
        const QRegularExpression m_signatureRegexp;
        const QRegularExpression m_methodNameRegexp;
    };
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 68, as local:signalslotdialog.cpp:SignatureDelegate::SignatureDelegate
namespace {
inline SignatureDelegate::SignatureDelegate(QObject * parent) :
        QStyledItemDelegate(parent),
        m_signatureRegexp(signatureRegExp),
        m_methodNameRegexp(methodNameRegExp)
    {
        Q_ASSERT(m_signatureRegexp.isValid());
        Q_ASSERT(m_methodNameRegexp.isValid());
    }
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 77, as local:signalslotdialog.cpp:SignatureDelegate::createEditor
namespace {
inline QWidget * SignatureDelegate::createEditor ( QWidget * parent, const QStyleOptionViewItem &option, const QModelIndex &index ) const
    {
        QWidget *rc = QStyledItemDelegate::createEditor(parent, option, index);
        QLineEdit *le = qobject_cast<QLineEdit *>(rc);
        Q_ASSERT(le);
        le->setValidator(new QRegularExpressionValidator(m_signatureRegexp, le));
        return rc;
    }
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 86, as local:signalslotdialog.cpp:SignatureDelegate::setModelData
namespace {
inline void SignatureDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index ) const
    {
        QLineEdit *le = qobject_cast<QLineEdit *>(editor);
        Q_ASSERT(le);
        // Did the user just type a name? .. Add parentheses
        QString signature = le->text();
        if (!m_signatureRegexp.match(signature).hasMatch()) {
            if (m_methodNameRegexp.match(signature).hasMatch()) {
                signature += "()"_L1;
                le->setText(signature);
            } else {
                return;
            }
        }
        QStyledItemDelegate::setModelData(editor, model, index);
    }
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 266, as _ZNK18qdesigner_internal14SignaturePanel11fakeMethodsEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QStringList SignaturePanel::fakeMethods() const
{
    QStringList rc;
    if (const int rowCount = m_model->rowCount())
        for (int  i = 0; i < rowCount; i++) {
            const QStandardItem *item =  m_model->item(i);
            if (item->flags() & Qt::ItemIsEditable)
                rc += item->text();
        }
    return rc;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 251, as _ZN18qdesigner_internal14SignaturePanel7setDataERKNS_20SignalSlotDialogDataE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::setData(const SignalSlotDialogData &d)
{
    m_model->clear();

    QStandardItem *lastExisting = nullptr;
    for (const QString &s : d.m_existingMethods) {
        lastExisting = createDisabledItem(s);
        m_model->appendRow(lastExisting);
    }
    for (const QString &s : d.m_fakeMethods)
        m_model->appendRow(createEditableItem(s));
    if (lastExisting)
        m_listView->scrollTo(m_model->indexFromItem(lastExisting));
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 226, as _ZNK18qdesigner_internal14SignaturePanel5countERK7QString
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline int SignaturePanel::count(const QString &signature) const
{
    return m_model->findItems(signature).size();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 278, as _ZN18qdesigner_internal14SignaturePanel11closeEditorEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::closeEditor()
{
    const QModelIndex idx = m_listView->currentIndex();
    if (idx.isValid())
        m_listView->closePersistentEditor(idx);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject *qdesigner_internal::SignaturePanel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14SignaturePanel10metaObjectEv(
    const qdesigner_internal::SignaturePanel *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::SignaturePanel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14SignaturePanel11qt_metacastEPKc(
    qdesigner_internal::SignaturePanel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::SignaturePanel::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14SignaturePanel11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::SignaturePanel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QStringList qdesigner_internal::SignaturePanel::fakeMethods() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal14SignaturePanel11fakeMethodsEv(
    const qdesigner_internal::SignaturePanel *self) {
  return new QList<QString>(self->fakeMethods());
}

//  void qdesigner_internal::SignaturePanel::setData(const
//      SignalSlotDialogData &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel7setDataERKNS_20SignalSlotDialogDataE(
    qdesigner_internal::SignaturePanel *self,
    const qdesigner_internal::SignalSlotDialogData *d) {
  self->setData(*d);
}

//  int qdesigner_internal::SignaturePanel::count(const QString &signature)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14SignaturePanel5countERK7QString(
    const qdesigner_internal::SignaturePanel *self,
    const QString *signature) {
  return self->count(*signature);
}

//  void qdesigner_internal::SignaturePanel::checkSignature(const QString
//      &signature, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel14checkSignatureERK7QStringPb(
    qdesigner_internal::SignaturePanel *self,
    const QString *signature,
    bool *ok) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkSignature(const QString &,bool *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkSignature(const QString &,bool *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(signature)),
      const_cast<void *>(static_cast<const void *>(&ok)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::slotAdd()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel7slotAddEv(
    qdesigner_internal::SignaturePanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
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

//  void qdesigner_internal::SignaturePanel::slotRemove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel10slotRemoveEv(
    qdesigner_internal::SignaturePanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotRemove()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotRemove()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::slotSelectionChanged(const
//      QItemSelection &a0, const QItemSelection &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel20slotSelectionChangedERK14QItemSelectionS3_(
    qdesigner_internal::SignaturePanel *self,
    const QItemSelection *a0,
    const QItemSelection *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotSelectionChanged(const QItemSelection &,const QItemSelection &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotSelectionChanged(const QItemSelection &,const QItemSelection &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::closeEditor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel11closeEditorEv(
    qdesigner_internal::SignaturePanel *self) {
  self->closeEditor();
}
