//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcompleter.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcompleter.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QCompleter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QCompleter10metaObjectEv(
    const QCompleter *self) {
  return self->metaObject();
}

//  QString QCompleter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QCompleter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCompleter::tr(s, c, n));
}

//  QCompleter::QCompleter(QObject *parent)
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN10QCompleterC1EP7QObject(QObject *parent) {
  return new QCompleter(parent);
}

//  QCompleter::QCompleter(QAbstractItemModel *model, QObject *parent)
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN10QCompleterC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *model,
    QObject *parent) {
  return new QCompleter(model, parent);
}

//  QCompleter::~QCompleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleterD1Ev(QCompleter *self) {
  delete self;
}

//  void QCompleter::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter9setWidgetEP7QWidget(
    QCompleter *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QCompleter::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QCompleter6widgetEv(const QCompleter *self) {
  return self->widget();
}

//  void QCompleter::setModel(QAbstractItemModel *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter8setModelEP18QAbstractItemModel(
    QCompleter *self,
    QAbstractItemModel *c) {
  self->setModel(c);
}

//  QAbstractItemModel *QCompleter::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK10QCompleter5modelEv(const QCompleter *self) {
  return self->model();
}

//  void QCompleter::setCompletionMode(CompletionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter17setCompletionModeENS_14CompletionModeE(
    QCompleter *self,
    QCompleter::CompletionMode mode) {
  self->setCompletionMode(mode);
}

//  CompletionMode QCompleter::completionMode() const
extern "C" Q_DECL_EXPORT
QCompleter::CompletionMode ritual_ZNK10QCompleter14completionModeEv(
    const QCompleter *self) {
  return self->completionMode();
}

//  void QCompleter::setFilterMode(Qt::MatchFlags filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter13setFilterModeE6QFlagsIN2Qt9MatchFlagEE(
    QCompleter *self,
    int filterMode) {
  self->setFilterMode(QFlags<Qt::MatchFlag>::fromInt(filterMode));
}

//  Qt::MatchFlags QCompleter::filterMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter10filterModeEv(const QCompleter *self) {
  return static_cast<int>(self->filterMode().toInt());
}

//  QAbstractItemView *QCompleter::popup() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK10QCompleter5popupEv(const QCompleter *self) {
  return self->popup();
}

//  void QCompleter::setPopup(QAbstractItemView *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter8setPopupEP17QAbstractItemView(
    QCompleter *self,
    QAbstractItemView *popup) {
  self->setPopup(popup);
}

//  void QCompleter::setCaseSensitivity(Qt::CaseSensitivity caseSensitivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QCompleter *self,
    Qt::CaseSensitivity caseSensitivity) {
  self->setCaseSensitivity(caseSensitivity);
}

//  Qt::CaseSensitivity QCompleter::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK10QCompleter15caseSensitivityEv(
    const QCompleter *self) {
  return self->caseSensitivity();
}

//  void QCompleter::setModelSorting(ModelSorting sorting)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter15setModelSortingENS_12ModelSortingE(
    QCompleter *self,
    QCompleter::ModelSorting sorting) {
  self->setModelSorting(sorting);
}

//  ModelSorting QCompleter::modelSorting() const
extern "C" Q_DECL_EXPORT
QCompleter::ModelSorting ritual_ZNK10QCompleter12modelSortingEv(
    const QCompleter *self) {
  return self->modelSorting();
}

//  void QCompleter::setCompletionColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter19setCompletionColumnEi(
    QCompleter *self,
    int column) {
  self->setCompletionColumn(column);
}

//  int QCompleter::completionColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter16completionColumnEv(const QCompleter *self) {
  return self->completionColumn();
}

//  void QCompleter::setCompletionRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter17setCompletionRoleEi(QCompleter *self, int role) {
  self->setCompletionRole(role);
}

//  int QCompleter::completionRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter14completionRoleEv(const QCompleter *self) {
  return self->completionRole();
}

//  bool QCompleter::wrapAround() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCompleter10wrapAroundEv(const QCompleter *self) {
  return self->wrapAround();
}

//  int QCompleter::maxVisibleItems() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter15maxVisibleItemsEv(const QCompleter *self) {
  return self->maxVisibleItems();
}

//  void QCompleter::setMaxVisibleItems(int maxItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter18setMaxVisibleItemsEi(
    QCompleter *self,
    int maxItems) {
  self->setMaxVisibleItems(maxItems);
}

//  int QCompleter::completionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter15completionCountEv(const QCompleter *self) {
  return self->completionCount();
}

//  bool QCompleter::setCurrentRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCompleter13setCurrentRowEi(QCompleter *self, int row) {
  return self->setCurrentRow(row);
}

//  int QCompleter::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter10currentRowEv(const QCompleter *self) {
  return self->currentRow();
}

//  QModelIndex QCompleter::currentIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QCompleter12currentIndexEv(const QCompleter *self) {
  return new QModelIndex(self->currentIndex());
}

//  QString QCompleter::currentCompletion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCompleter17currentCompletionEv(
    const QCompleter *self) {
  return new QString(self->currentCompletion());
}

//  QAbstractItemModel *QCompleter::completionModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK10QCompleter15completionModelEv(
    const QCompleter *self) {
  return self->completionModel();
}

//  QString QCompleter::completionPrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCompleter16completionPrefixEv(const QCompleter *self) {
  return new QString(self->completionPrefix());
}

//  void QCompleter::setCompletionPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter19setCompletionPrefixERK7QString(
    QCompleter *self,
    const QString *prefix) {
  self->setCompletionPrefix(*prefix);
}

//  void QCompleter::complete(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter8completeERK5QRect(
    QCompleter *self,
    const QRect *rect) {
  self->complete(*rect);
}

//  void QCompleter::setWrapAround(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter13setWrapAroundEb(QCompleter *self, bool wrap) {
  self->setWrapAround(wrap);
}

//  QString QCompleter::pathFromIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCompleter13pathFromIndexERK11QModelIndex(
    const QCompleter *self,
    const QModelIndex *index) {
  return new QString(self->pathFromIndex(*index));
}
