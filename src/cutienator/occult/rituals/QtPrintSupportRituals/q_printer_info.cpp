//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/qprinterinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/qprinterinfo.h>
#include <QtCore/qstring.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QPrinterInfo::QPrinterInfo()
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_ZN12QPrinterInfoC1Ev() {
  return new QPrinterInfo();
}

//  QPrinterInfo::QPrinterInfo(const QPrinterInfo &other)
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_ZN12QPrinterInfoC1ERKS_(const QPrinterInfo *other) {
  return new QPrinterInfo(*other);
}

//  QPrinterInfo::~QPrinterInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrinterInfoD1Ev(QPrinterInfo *self) {
  delete self;
}

//  QString QPrinterInfo::printerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrinterInfo11printerNameEv(const QPrinterInfo *self) {
  return new QString(self->printerName());
}

//  QString QPrinterInfo::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrinterInfo11descriptionEv(const QPrinterInfo *self) {
  return new QString(self->description());
}

//  QString QPrinterInfo::location() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrinterInfo8locationEv(const QPrinterInfo *self) {
  return new QString(self->location());
}

//  QString QPrinterInfo::makeAndModel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrinterInfo12makeAndModelEv(const QPrinterInfo *self) {
  return new QString(self->makeAndModel());
}

//  bool QPrinterInfo::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrinterInfo6isNullEv(const QPrinterInfo *self) {
  return self->isNull();
}

//  bool QPrinterInfo::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrinterInfo9isDefaultEv(const QPrinterInfo *self) {
  return self->isDefault();
}

//  bool QPrinterInfo::isRemote() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrinterInfo8isRemoteEv(const QPrinterInfo *self) {
  return self->isRemote();
}

//  QPrinter::PrinterState QPrinterInfo::state() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_ZNK12QPrinterInfo5stateEv(
    const QPrinterInfo *self) {
  return self->state();
}

//  QList<QPageSize> QPrinterInfo::supportedPageSizes() const
extern "C" Q_DECL_EXPORT
QList<QPageSize> *ritual_ZNK12QPrinterInfo18supportedPageSizesEv(
    const QPrinterInfo *self) {
  return new QList<QPageSize>(self->supportedPageSizes());
}

//  QPageSize QPrinterInfo::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrinterInfo15defaultPageSizeEv(
    const QPrinterInfo *self) {
  return new QPageSize(self->defaultPageSize());
}

//  bool QPrinterInfo::supportsCustomPageSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrinterInfo23supportsCustomPageSizesEv(
    const QPrinterInfo *self) {
  return self->supportsCustomPageSizes();
}

//  QPageSize QPrinterInfo::minimumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrinterInfo23minimumPhysicalPageSizeEv(
    const QPrinterInfo *self) {
  return new QPageSize(self->minimumPhysicalPageSize());
}

//  QPageSize QPrinterInfo::maximumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrinterInfo23maximumPhysicalPageSizeEv(
    const QPrinterInfo *self) {
  return new QPageSize(self->maximumPhysicalPageSize());
}

//  QPrinter::DuplexMode QPrinterInfo::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrinter::DuplexMode ritual_ZNK12QPrinterInfo17defaultDuplexModeEv(
    const QPrinterInfo *self) {
  return self->defaultDuplexMode();
}

//  QPrinter::ColorMode QPrinterInfo::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrinter::ColorMode ritual_ZNK12QPrinterInfo16defaultColorModeEv(
    const QPrinterInfo *self) {
  return self->defaultColorMode();
}

//  QStringList QPrinterInfo::availablePrinterNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN12QPrinterInfo21availablePrinterNamesEv() {
  return new QList<QString>(QPrinterInfo::availablePrinterNames());
}

//  QList<QPrinterInfo> QPrinterInfo::availablePrinters()
extern "C" Q_DECL_EXPORT
QList<QPrinterInfo> *ritual_ZN12QPrinterInfo17availablePrintersEv() {
  return new QList<QPrinterInfo>(QPrinterInfo::availablePrinters());
}

//  QString QPrinterInfo::defaultPrinterName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QPrinterInfo18defaultPrinterNameEv() {
  return new QString(QPrinterInfo::defaultPrinterName());
}

//  QPrinterInfo QPrinterInfo::defaultPrinter()
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_ZN12QPrinterInfo14defaultPrinterEv() {
  return new QPrinterInfo(QPrinterInfo::defaultPrinter());
}

//  QPrinterInfo QPrinterInfo::printerInfo(const QString &printerName)
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_ZN12QPrinterInfo11printerInfoERK7QString(
    const QString *printerName) {
  return new QPrinterInfo(QPrinterInfo::printerInfo(*printerName));
}

//  QPrinterInfo::QPrinterInfo(const QString &name)
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_ZN12QPrinterInfoC1ERK7QString(const QString *name) {
  return new QPrinterInfo(*name);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QPrinterInfo &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK12QPrinterInfo(
    const QDebug *debug,
    const QPrinterInfo *a1) {
  return new QDebug(operator<<(*debug, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QPrinterInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QPrinterInfo> *ritual_list_make_QPrinterInfo() {
  return new QList<QPrinterInfo>();
}

//  void QList<QPrinterInfo>::append(const QPrinterInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPrinterInfo(
    QList<QPrinterInfo> *self,
    const QPrinterInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QPrinterInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPrinterInfo(const QList<QPrinterInfo> *self) {
  return self->size();
}

//  const QPrinterInfo &QList<QPrinterInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_list_at_QPrinterInfo(
    const QList<QPrinterInfo> *self,
    long long index) {
  return new QPrinterInfo(self->at(index));
}

//  QList<QPrinterInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPrinterInfo(QList<QPrinterInfo> *self) {
  delete self;
}

#endif  // !defined(QT_NO_PRINTER)
