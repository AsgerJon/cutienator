//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlogging.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand: 'ritual_ZNK14QMessageLogger5debugEPKcz',
//  'ritual_ZNK14QMessageLogger5debugERK16QLoggingCategoryPKcz',
//  'ritual_ZNK14QMessageLogger5debugEPFRK16QLoggingCategoryvEPKcz',
//  'ritual_ZNK14QMessageLogger7noDebugEPKcz',
//  'ritual_ZNK14QMessageLogger4infoEPKcz',
//  'ritual_ZNK14QMessageLogger4infoERK16QLoggingCategoryPKcz',
//  'ritual_ZNK14QMessageLogger4infoEPFRK16QLoggingCategoryvEPKcz',
//  'ritual_ZNK14QMessageLogger7warningEPKcz',
//  'ritual_ZNK14QMessageLogger7warningERK16QLoggingCategoryPKcz',
//  'ritual_ZNK14QMessageLogger7warningEPFRK16QLoggingCategoryvEPKcz',
//  'ritual_ZNK14QMessageLogger8criticalEPKcz',
//  'ritual_ZNK14QMessageLogger8criticalERK16QLoggingCategoryPKcz',
//  'ritual_ZNK14QMessageLogger8criticalEPFRK16QLoggingCategoryvEPKcz',
//  'ritual_ZNK14QMessageLogger5fatalEPKcz',
//  'ritual_ZNK14QMessageLogger5fatalERK16QLoggingCategoryPKcz',
//  'ritual_ZNK14QMessageLogger5fatalEPFRK16QLoggingCategoryvEPKcz',
//  'ritual_ZNK14QMessageLogger7noDebugEz'. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>

//  QMessageLogger::QMessageLogger()
extern "C" Q_DECL_EXPORT
QMessageLogger *ritual_ZN14QMessageLoggerC1Ev() {
  return new QMessageLogger();
}

//  QMessageLogger::QMessageLogger(const char *file, int line, const char
//      *function)
extern "C" Q_DECL_EXPORT
QMessageLogger *ritual_ZN14QMessageLoggerC1EPKciS1_(
    const char *file,
    int line,
    const char *function) {
  return new QMessageLogger(file, line, function);
}

//  QMessageLogger::QMessageLogger(const char *file, int line, const char
//      *function, const char *category)
extern "C" Q_DECL_EXPORT
QMessageLogger *ritual_ZN14QMessageLoggerC1EPKciS1_S1_(
    const char *file,
    int line,
    const char *function,
    const char *category) {
  return new QMessageLogger(file, line, function, category);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::debug() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5debugEv(const QMessageLogger *self) {
  return new QDebug(self->debug());
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::debug(const QLoggingCategory &cat) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5debugERK16QLoggingCategory(
    const QMessageLogger *self,
    const QLoggingCategory *cat) {
  return new QDebug(self->debug(*cat));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::debug(CategoryFunction catFunc) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5debugEPFRK16QLoggingCategoryvE(
    const QMessageLogger *self,
    void *catFunc) {
  return new QDebug(
      self->debug(
          reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc)));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::info() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger4infoEv(const QMessageLogger *self) {
  return new QDebug(self->info());
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::info(const QLoggingCategory &cat) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger4infoERK16QLoggingCategory(
    const QMessageLogger *self,
    const QLoggingCategory *cat) {
  return new QDebug(self->info(*cat));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::info(CategoryFunction catFunc) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger4infoEPFRK16QLoggingCategoryvE(
    const QMessageLogger *self,
    void *catFunc) {
  return new QDebug(
      self->info(
          reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc)));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::warning() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger7warningEv(const QMessageLogger *self) {
  return new QDebug(self->warning());
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::warning(const QLoggingCategory &cat) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger7warningERK16QLoggingCategory(
    const QMessageLogger *self,
    const QLoggingCategory *cat) {
  return new QDebug(self->warning(*cat));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::warning(CategoryFunction catFunc) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger7warningEPFRK16QLoggingCategoryvE(
    const QMessageLogger *self,
    void *catFunc) {
  return new QDebug(
      self->warning(
          reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc)));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::critical() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger8criticalEv(const QMessageLogger *self) {
  return new QDebug(self->critical());
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::critical(const QLoggingCategory &cat) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger8criticalERK16QLoggingCategory(
    const QMessageLogger *self,
    const QLoggingCategory *cat) {
  return new QDebug(self->critical(*cat));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::critical(CategoryFunction catFunc) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger8criticalEPFRK16QLoggingCategoryvE(
    const QMessageLogger *self,
    void *catFunc) {
  return new QDebug(
      self->critical(
          reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc)));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::fatal() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5fatalEv(const QMessageLogger *self) {
  return new QDebug(self->fatal());
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::fatal(const QLoggingCategory &cat) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5fatalERK16QLoggingCategory(
    const QMessageLogger *self,
    const QLoggingCategory *cat) {
  return new QDebug(self->fatal(*cat));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QMessageLogger::fatal(CategoryFunction catFunc) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5fatalEPFRK16QLoggingCategoryvE(
    const QMessageLogger *self,
    void *catFunc) {
  return new QDebug(
      self->fatal(
          reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc)));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  void QMessageLogger::debug(const char *msg, ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger5debugEPKcz(
    const QMessageLogger *self,
    const char *text) {
  self->debug("%s", text);
}

//  void QMessageLogger::debug(const QLoggingCategory &cat, const char *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger5debugERK16QLoggingCategoryPKcz(
    const QMessageLogger *self,
    const QLoggingCategory *cat,
    const char *text) {
  self->debug(*cat, "%s", text);
}

//  void QMessageLogger::debug(CategoryFunction catFunc, const char *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger5debugEPFRK16QLoggingCategoryvEPKcz(
    const QMessageLogger *self,
    void *catFunc,
    const char *text) {
  self->debug(
      reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc),
      "%s", text);
}

//  void QMessageLogger::noDebug(const char *, ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger7noDebugEPKcz(
    const QMessageLogger *self,
    const char *text) {
  self->noDebug("%s", text);
}

//  void QMessageLogger::info(const char *msg, ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger4infoEPKcz(
    const QMessageLogger *self,
    const char *text) {
  self->info("%s", text);
}

//  void QMessageLogger::info(const QLoggingCategory &cat, const char *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger4infoERK16QLoggingCategoryPKcz(
    const QMessageLogger *self,
    const QLoggingCategory *cat,
    const char *text) {
  self->info(*cat, "%s", text);
}

//  void QMessageLogger::info(CategoryFunction catFunc, const char *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger4infoEPFRK16QLoggingCategoryvEPKcz(
    const QMessageLogger *self,
    void *catFunc,
    const char *text) {
  self->info(
      reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc),
      "%s", text);
}

//  void QMessageLogger::warning(const char *msg, ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger7warningEPKcz(
    const QMessageLogger *self,
    const char *text) {
  self->warning("%s", text);
}

//  void QMessageLogger::warning(const QLoggingCategory &cat, const char
//      *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger7warningERK16QLoggingCategoryPKcz(
    const QMessageLogger *self,
    const QLoggingCategory *cat,
    const char *text) {
  self->warning(*cat, "%s", text);
}

//  void QMessageLogger::warning(CategoryFunction catFunc, const char *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger7warningEPFRK16QLoggingCategoryvEPKcz(
    const QMessageLogger *self,
    void *catFunc,
    const char *text) {
  self->warning(
      reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc),
      "%s", text);
}

//  void QMessageLogger::critical(const char *msg, ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger8criticalEPKcz(
    const QMessageLogger *self,
    const char *text) {
  self->critical("%s", text);
}

//  void QMessageLogger::critical(const QLoggingCategory &cat, const char
//      *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger8criticalERK16QLoggingCategoryPKcz(
    const QMessageLogger *self,
    const QLoggingCategory *cat,
    const char *text) {
  self->critical(*cat, "%s", text);
}

//  void QMessageLogger::critical(CategoryFunction catFunc, const char
//      *msg,
//      ...) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger8criticalEPFRK16QLoggingCategoryvEPKcz(
    const QMessageLogger *self,
    void *catFunc,
    const char *text) {
  self->critical(
      reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc),
      "%s", text);
}

//  void QMessageLogger::fatal(const char *msg, ...) const noexcept
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger5fatalEPKcz(
    const QMessageLogger *self,
    const char *text) {
  self->fatal("%s", text);
}

//  void QMessageLogger::fatal(const QLoggingCategory &cat, const char *msg,
//      ...) const noexcept
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger5fatalERK16QLoggingCategoryPKcz(
    const QMessageLogger *self,
    const QLoggingCategory *cat,
    const char *text) {
  self->fatal(*cat, "%s", text);
}

//  void QMessageLogger::fatal(CategoryFunction catFunc, const char *msg,
//      ...) const noexcept
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger5fatalEPFRK16QLoggingCategoryvEPKcz(
    const QMessageLogger *self,
    void *catFunc,
    const char *text) {
  self->fatal(
      reinterpret_cast<QMessageLogger::CategoryFunction>(catFunc),
      "%s", text);
}

//  QNoDebug QMessageLogger::noDebug(...) const noexcept
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMessageLogger7noDebugEz(const QMessageLogger *self) {
  self->noDebug();
}
