//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextoption.h>
#include <QtCore/QList>
#include <QtGui/QTextOption>

//  QTextOption::QTextOption()
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZN11QTextOptionC1Ev() {
  return new QTextOption();
}

//  QTextOption::QTextOption(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZN11QTextOptionC1E6QFlagsIN2Qt13AlignmentFlagEE(
    int alignment) {
  return new QTextOption(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QTextOption::~QTextOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOptionD1Ev(QTextOption *self) {
  delete self;
}

//  QTextOption::QTextOption(const QTextOption &o)
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZN11QTextOptionC1ERKS_(const QTextOption *o) {
  return new QTextOption(*o);
}

//  QTextOption &QTextOption::operator=(const QTextOption &o)
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZN11QTextOptionaSERKS_(
    QTextOption *self,
    const QTextOption *o) {
  return &(self->operator=(*o));
}

//  void QTextOption::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTextOption *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QTextOption::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextOption9alignmentEv(const QTextOption *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QTextOption::setTextDirection(Qt::LayoutDirection aDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption16setTextDirectionEN2Qt15LayoutDirectionE(
    QTextOption *self,
    Qt::LayoutDirection aDirection) {
  self->setTextDirection(aDirection);
}

//  Qt::LayoutDirection QTextOption::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK11QTextOption13textDirectionEv(
    const QTextOption *self) {
  return self->textDirection();
}

//  void QTextOption::setWrapMode(WrapMode wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption11setWrapModeENS_8WrapModeE(
    QTextOption *self,
    QTextOption::WrapMode wrap) {
  self->setWrapMode(wrap);
}

//  WrapMode QTextOption::wrapMode() const
extern "C" Q_DECL_EXPORT
QTextOption::WrapMode ritual_ZNK11QTextOption8wrapModeEv(
    const QTextOption *self) {
  return self->wrapMode();
}

//  void QTextOption::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption8setFlagsE6QFlagsINS_4FlagEE(
    QTextOption *self,
    int flags) {
  self->setFlags(QFlags<QTextOption::Flag>::fromInt(flags));
}

//  Flags QTextOption::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextOption5flagsEv(const QTextOption *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QTextOption::setTabStopDistance(qreal tabStopDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption18setTabStopDistanceEd(
    QTextOption *self,
    qreal tabStopDistance) {
  self->setTabStopDistance(tabStopDistance);
}

//  qreal QTextOption::tabStopDistance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QTextOption15tabStopDistanceEv(const QTextOption *self) {
  return self->tabStopDistance();
}

//  void QTextOption::setTabArray(const QList<qreal> &tabStops)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption11setTabArrayERK5QListIdE(
    QTextOption *self,
    const QList<qreal> *tabStops) {
  self->setTabArray(*tabStops);
}

//  QList<qreal> QTextOption::tabArray() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK11QTextOption8tabArrayEv(const QTextOption *self) {
  return new QList<qreal>(self->tabArray());
}

//  void QTextOption::setTabs(const QList<Tab> &tabStops)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption7setTabsERK5QListINS_3TabEE(
    QTextOption *self,
    const QList<QTextOption::Tab> *tabStops) {
  self->setTabs(*tabStops);
}

//  QList<Tab> QTextOption::tabs() const
extern "C" Q_DECL_EXPORT
QList<QTextOption::Tab> *ritual_ZNK11QTextOption4tabsEv(
    const QTextOption *self) {
  return new QList<QTextOption::Tab>(self->tabs());
}

//  void QTextOption::setUseDesignMetrics(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption19setUseDesignMetricsEb(
    QTextOption *self,
    bool b) {
  self->setUseDesignMetrics(b);
}

//  bool QTextOption::useDesignMetrics() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextOption16useDesignMetricsEv(const QTextOption *self) {
  return self->useDesignMetrics();
}

//  a QList<qreal> a ritual of QTextOption gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextOption__QList_qreal(QList<qreal> *self) {
  delete self;
}

//  a QList<QTextOption::Tab> a ritual of QTextOption gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextOption__QList_QTextOption_Tab(
    QList<QTextOption::Tab> *self) {
  delete self;
}
